# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, lurl, redirect, tmpl_context
from tg.i18n import ugettext as _, set_lang
from parsidan import model
from parsidan.controllers.dictionary import DictionaryController
from parsidan.model import Dictionary, DBSession, PersianWord, ForeignWord
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
import transaction
from parsidan.controllers.authentication import AuthenticationController
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
    authentication = AuthenticationController()

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

    @expose()
    def login(self, came_from=lurl('/')):
        redirect('/authentication/login', params=dict(came_from=came_from))


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
