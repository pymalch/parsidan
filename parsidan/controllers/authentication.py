# -*- coding: utf-8 -*-

from tg import expose, flash, url, lurl, request, redirect, require
from tg.i18n import ugettext as _
from tg.exceptions import HTTPFound
from parsidan.model import User, DBSession
from parsidan.forms.authentication import LoginForm, RegistrationForm, ChangePasswordForm, RecoverPasswordForm
from tg.decorators import validate
from parsidan.lib.base import BaseController
from parsidan.exceptions.authentication import VerificationError
import transaction
from tg.predicates import not_anonymous
__author__ = 'vahid'

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
            flash(_('Invalid username or password'), 'error')
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

    @expose("parsidan.templates.authentication.verification_request")
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
                            status='confirmed')

            new_user.password = password
            DBSession.add(new_user)
            DBSession.flush()
            new_user.request_activation()
            transaction.commit()
            return dict(user=new_user)

    @expose("parsidan.templates.authentication.verification_success")
    def verify(self, user=None, activation_code=None):
        # TODO: exception handling
        email = user
        user = User.by_email(email)
        if not user:
            flash(_('Invalid username/email address.'), 'error')
            return HTTPFound(location=url('verification_error', params=dict(user=email)))
        else:
            try:
                user.complete_activation(activation_code)
                transaction.commit()
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
        transaction.commit()
        return dict(user=user)

    @expose("parsidan.templates.authentication.change_password")
    @require(not_anonymous(msg=_('Only logged in users can change their password')))
    def change_password_form(self, *args, **kwargs):
        form = ChangePasswordForm.req()
        return dict(form=form)

    @expose("parsidan.templates.authentication.change_password_success")
    @require(not_anonymous(msg=_('Only logged in users can change their password')))
    @validate(ChangePasswordForm, error_handler=change_password_form)
    def change_password(self, current_password=None, new_password=None, password_confirm=None):
        email = request.identity['repoze.who.userid']
        user = User.by_email(email)
        if user.validate_password(current_password):
            user.password = new_password
            transaction.commit()
        else:
            flash(_('Invalid current password'), 'error')
            redirect('change_password_form')
        return dict(user=user)

    @expose("parsidan.templates.authentication.password_recovery")
    def recover_password_form(self, *args, **kwargs):
        form = RecoverPasswordForm.req()
        return dict(form=form)

    @expose("parsidan.templates.authentication.password_recovery_success")
    @validate(RecoverPasswordForm, error_handler=recover_password_form)
    def recover_password(self, email=None, *args, **kw):
        user = User.by_email(email)
        if user:
            user.reset_password()
            transaction.commit()
        else:
            flash(_('Invalid email address'), 'error')
            redirect('recover_password_form')
        return dict(user=user)