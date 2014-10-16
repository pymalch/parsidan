# -*- coding: utf-8 -*-
from parsidan.exceptions.authentication import VerificationError

__author__ = 'vahid'
# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, url, lurl, request, redirect
from tg.i18n import ugettext as _
from tg.exceptions import HTTPFound
from parsidan.model import User, DBSession
from parsidan.forms.authentication import LoginForm, RegistrationForm
from tg.decorators import validate
from parsidan.lib.base import BaseController


__all__ = ['AuthenticationController']


class AuthenticationController(BaseController):
    @expose('parsidan.templates.authentication.login')
    # @validate(LoginForm, error_handler=login)
    def login(self, came_from=lurl('/')):
        """Start the user login."""
        login_counter = request.environ.get('repoze.who.logins', 0)
        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        login_form = LoginForm.req()
        login_form.action = url('/login_handler', params=dict(came_from=came_from, __logins=login_counter))
        return dict(login_counter=str(login_counter),
                    came_from=came_from, form=login_form)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            #login_counter = request.environ.get('repoze.who.logins', 0) + 1
            flash(_('Invalid username or password'))
            redirect('login',
                     params=dict(came_from=came_from))
        userid = request.identity['repoze.who.userid']
        flash(_('Welcome back, %s!') % userid)

        # Do not use tg.redirect with tg.url as it will add the mountpoint
        # of the application twice.
        return HTTPFound(location=came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        return HTTPFound(location=came_from)

    @expose("parsidan.templates.authentication.signup")
    def signup_form(self, *args, **kwargs):
        """Start the user login."""

        signup_form = RegistrationForm.req()
        return dict(form=signup_form)

    @expose("parsidan.templates.authentication.signup_success")
    @validate(RegistrationForm, error_handler=signup_form)
    def signup(self, email=None, nickname=None, password=None, password_confirm=None, *args, **kw):
        # TODO: exception handling
        email = email.strip()
        if User.by_email(email):
            flash(_('The submitted email address, is alreday precent in our database.'), 'error')
            redirect('signup_form')
        else:
            new_user = User(email=email,
                            nickname=nickname,
                            status='pending')

            new_user.password = password;
            DBSession.add(new_user)
            DBSession.flush()
            # transaction.commit()

            new_user.request_activation()

            return dict(user=new_user)

    @expose("parsidan.templates.authentication.verification_success")
    def verify(self, user=None, activation_code=None):
        # TODO: exception handling
        user = User.by_email(user)
        if not user:
            flash(_('Invalid username/email address.'), 'error')
            return HTTPFound(location=url('verification_error', params=dict(user=user.email)))
        else:
            try:
                user.complete_activation(activation_code)
                return dict(user=user)
            except VerificationError as ex:
                flash(ex.message, 'error')
                return HTTPFound(location=url('verification_error', params=dict(user=user.email)))


    @expose("parsidan.templates.authentication.verification_error")
    def verification_error(self, user=None):
        return dict(user=User.by_email(user))

    @expose("parsidan.templates.authentication.verification_request")
    def resend_verification_request(self, user=None):
        user = User.by_email(user)
        if not user:
            flash(_('Invalid username/email address.'), 'error')
            return HTTPFound(location=url('verification_error', params=dict(user=user.email)))

        user.request_activation()
        return dict(user=None)
