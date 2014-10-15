# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_, set_lang
from tg.exceptions import HTTPFound
from parsidan import model
from parsidan.controllers.dictionary import DictionaryController
from parsidan.model import Dictionary, DBSession, PersianWord, ForeignWord, User
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
import transaction
from parsidan.forms.auth import LoginForm, RegistrationForm
from tg.decorators import validate
from sqlalchemy.exc import IntegrityError

from parsidan.lib.base import BaseController
from parsidan.controllers.error import ErrorController


__all__ = ['RootController']

class QueryStatus:
    success = 0
    not_found = 1
    persian_word = 2



class RootController(BaseController):

    dictionary = DictionaryController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)
    error = ErrorController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = _("parsidan")

    @expose('parsidan.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(word='',
                    result=None)

    @expose()
    def setlang(self, lang, camefrom=lurl('/')):
        if lang:
            set_lang(lang)
        redirect(camefrom)

    @expose('parsidan.templates.auth.login')
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
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                params=dict(came_from=came_from, __logins=login_counter))
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

    @expose('parsidan.templates.index')
    @expose('json')
    def query(self, word=None):
        result = list(Dictionary.query(word))
        if not len(result):
            if PersianWord.find(word):
                return dict(word=word, status=QueryStatus.persian_word)
            else:
                ForeignWord.check_and_hit(word)
                #DBSession.commit()
                transaction.commit()
                return dict(word=word, status=QueryStatus.not_found)
        else:
            ForeignWord.hit(word)
            #DBSession.commit()
            transaction.commit()
            return dict(word=word, status=QueryStatus.success, result=result)


    @expose("parsidan.templates.auth.signup")
    def signup_form(self, *args, **kwargs):
        """Start the user login."""

        signup_form = RegistrationForm.req()
        return dict(form=signup_form)

    @expose("parsidan.templates.auth.signup_success")
    @validate(RegistrationForm, error_handler=signup_form)
    def signup(self, email=None, nickname=None, password=None, password_confirm=None, *args, **kw):

        email = email.strip()
        if User.by_email(email):
            flash(_('The submitted email address, is alreday precent in our database.'), 'error ')
            redirect('/signup_form')
        else:
            new_user = User(email=email,
                           nickname=nickname,
                           status='pending')

            new_user.password = password;
            DBSession.add(new_user)
            transaction.commit()
            return dict(user=new_user)



