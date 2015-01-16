# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by the authentication stack are defined.

It's perfectly fine to re-use this definition in the parsidan application,
though.

"""
import os
from datetime import datetime
from hashlib import sha256, sha1
from parsidan.exceptions.authentication import VerificationError
from tg.i18n import ugettext as _
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime
from sqlalchemy.orm import relation, synonym
from parsidan.model import DeclarativeBase, metadata, DBSession
from parsidan.model.mixins import ConfirmableMixin, TimestampMixin
from parsidan.mailing import Mailer
import tg
from random import random
import transaction

__all__ = ['User', 'Group', 'Permission']

# This is the association table for the many-to-many relationship between
# groups and permissions.
group_permission_table = Table('group_permission', metadata,
    Column('group_id', Integer, ForeignKey('group.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permission.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)

# This is the association table for the many-to-many relationship between
# groups and members - this is, the memberships.
user_group_table = Table('user_group', metadata,
    Column('user_id', Integer, ForeignKey('user.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('group_id', Integer, ForeignKey('group.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)


class Group(TimestampMixin, DeclarativeBase):
    """
    Group definition

    Only the ``group_name`` column is required.

    """

    __tablename__ = 'group'

    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Unicode(16), unique=True, nullable=False)
    created = Column(DateTime, default=datetime.now)
    users = relation('User', secondary=user_group_table, backref='groups')

    def __repr__(self):
        return '<Group: name=%s>' % repr(self.title)

    def __unicode__(self):
        return self.title

class User(TimestampMixin, ConfirmableMixin, DeclarativeBase):
    """
    User definition.

    This is the user definition used by :mod:`repoze.who`, which requires at
    least the ``user_name`` column.

    """
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq', start=1001, increment=1) , primary_key=True)
    email = Column(Unicode(255), unique=True, nullable=False)
    nickname = Column(Unicode(255))
    activation_request_time = Column(DateTime, nullable=True)
    _password = Column('password', Unicode(128))

    def __repr__(self):
        return '<User: email=%s, display=%s>' % (
                repr(self.email), repr(self.nickname))

    def __unicode__(self):
        return self.nickname or self.email

    @property
    def permissions(self):
        """Return a set with all permissions granted to the user."""
        perms = set()
        for g in self.groups:
            perms = perms | set(g.permissions)
        return perms

    @classmethod
    def by_email(cls, email):
        """Return the user object whose email address is ``email``."""
        return DBSession.query(cls).filter_by(email=email).first()

    @classmethod
    def _hash_password(cls, password):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()

        hash = sha256()
        # Make sure password is a str because we cannot hash unicode objects
        hash.update((password + salt).encode('utf-8'))
        hash = hash.hexdigest()

        password = salt + hash

        # Make sure the hashed password is a unicode object at the end of the
        # process because SQLAlchemy _wants_ unicode objects for Unicode cols
        password = password.decode('utf-8')

        return password

    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        self._password = self._hash_password(password)

    def _get_password(self):
        """Return the hashed version of the password."""
        return self._password

    password = synonym('_password', descriptor=property(_get_password,
                                                        _set_password))

    def validate_password(self, password):
        """
        Check the password against existing credentials.

        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool

        """
        hash = sha256()
        hash.update((password + self.password[:64]).encode('utf-8'))
        return self.password[64:] == hash.hexdigest()

    @property
    def activation_code(self):
        if not self.activation_request_time:
            raise VerificationError(_("user already activated"))
        hash = sha256()
        hash.update(self.entry_time.strftime('%Y%m%d%h%M%s%f'))
        hash.update(self.activation_request_time.strftime('%Y%m%d%h%M%s%f'))
        hash.update(str(self.id))
        return hash.hexdigest()

    def request_activation(self, method='email'):
        self.activation_request_time = datetime.now()
        if method=='email':
            mailer = Mailer()
            mailer.send_template(self.email,
                                 _('Parsidan -- verify your email address'),
                                 template="parsidan.mailing.templates.activation_request",
                                 user=self,
                                 activation_code=self.activation_code,
                                 action="/authentication/verify",
                                 domain=tg.config.get("domain.name"))
        elif method=='sms':
            # TODO: sms verification
            pass
        elif method=='console':
            print "#" * 30
            print self.activation_code
            print "#" * 30
        else:
            raise ValueError(_("Invalid method value: %s") % method)

    def complete_activation(self, code):

        if not self.activation_request_time:
            raise VerificationError(_("user already activated"))

        timeout = int(tg.config.get("activation.timeout", 20)) # minutes

        if (datetime.now() - self.activation_request_time).total_seconds() / 60 >= timeout :
            raise VerificationError(_("Activation session expired, Resend activation code"))

        if code == self.activation_code:
            self.activation_request_time = None
            DBSession.flush()
        else:
            raise VerificationError(_("invalid activation code"))

    def reset_password(self, inform_method='email'):
        hash = sha1()
        hash.update(str(random()))
        new_password = hash.hexdigest()[:10]
        self.password = new_password
        transaction.commit()
        if inform_method=='email':
            mailer = Mailer()
            mailer.send_template(self.email,
                                 _('Parsidan -- your password has been reset.'),
                                 template="parsidan.mailing.templates.password_reset",
                                 user=self,
                                 new_password=new_password,
                                 action="/authentication/change_password_form",
                                 domain=tg.config.get("domain.name"))
        elif inform_method=='sms':
            # TODO: sms verification
            pass
        elif inform_method=='console':
            print "#" * 30
            print new_password
            print "#" * 30
        else:
            raise ValueError(_("Invalid method value: %s") % inform_method)


class Permission(DeclarativeBase):
    """
    Permission definition.

    Only the ``permission_name`` column is required.

    """

    __tablename__ = 'permission'


    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(Unicode(63), unique=True, nullable=False)
    description = Column(Unicode(255))

    groups = relation(Group, secondary=group_permission_table,
                      backref='permissions')

    def __repr__(self):
        return '<Permission: name=%s>' % repr(self.title)

    def __unicode__(self):
        return self.title
