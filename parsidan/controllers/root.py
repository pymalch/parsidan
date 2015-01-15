# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, lurl, redirect, tmpl_context, request
from tg.i18n import ugettext as _, set_lang
from tg.decorators import paginate as paginatedeco
from parsidan import model
from parsidan.model import Dictionary, DBSession, PersianWord, ForeignWord, QueryStatus
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController
import transaction
from parsidan.controllers.authentication import AuthenticationController
from parsidan.lib.base import BaseController
from parsidan.controllers.error import ErrorController
from parsidan.lib.sanitizer import sanitize
from parsidan.controllers.contribution import ContributionController

__all__ = ['RootController']




class RootController(BaseController):

    error = ErrorController()
    authentication = AuthenticationController()
    contribution = ContributionController()
    admin = AdminController(model, DBSession, config_type=TGAdminConfig)

    def _before(self, *args, **kw):
        tmpl_context.project_name = _("parsidan")

    @expose('parsidan.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(word='',
                    result=None)

    @expose()
    def setlang(self, lang, came_from=lurl('/')):
        if lang:
            set_lang(lang)
        redirect(came_from)

    @expose()
    def login(self, came_from=lurl('/')):
        redirect('/authentication/login', params=dict(came_from=came_from))


    @expose('parsidan.templates.index')
    @expose('json')
    def query(self, word=None):
        import time
        time.sleep(2)
        word = sanitize(word)
        result = list(Dictionary.query_persian(word))
        if not len(result):
            if PersianWord.find(word):
                result = list(Dictionary.query_foreign(word))
                return dict(word=word, status=QueryStatus.dictionary_persian_word, result=result)
            else:
                return dict(word=word, status=QueryStatus.dictionary_not_found)
        else:
            #todo
            return dict(word=word, status=QueryStatus.dictionary_foreign_word, result=result)

    @expose("parsidan.templates.contribution.words")
    @paginatedeco("words", items_per_page=10)
    def words(self, character=None, page=1, self_words=None):
        if character:
            character = sanitize(character)

        if request.identity and self_words:
            self_words = request.identity['user'].id

        words = PersianWord.list(character, self_words)

        return dict(words=words, alphabets=PersianWord.alphabets, character=character, self_words=self_words)