# -*- coding: utf-8 -*-

from tg import expose, flash, url, lurl, request, redirect, require
from tg.i18n import ugettext as _, lazy_ugettext as l_
from parsidan.model import User,PersianWord, ForeignWord, Dictionary
from parsidan.forms.contribution import SubmitWordForm
from tg.decorators import validate
from parsidan.lib.base import BaseController
import transaction
from tg.predicates import not_anonymous
__author__ = 'vahid'

__all__ = ['ContributionController']

class QueryStatus:
    success = 0
    added_before = 1
    foreign_word = 2

class ContributionController(BaseController):

    allow_only = not_anonymous(msg=l_('Please login to view this page.'))

    @expose("parsidan.templates.contribution.index")
    def index(self):
        return dict()


    @expose("json")
    def submit_persian_word(self, word):
        import time
        time.sleep(1)


        if PersianWord.find(word):
            result = list(Dictionary.find_persian_equivalents(word))
            return dict(word=word , status=QueryStatus.added_before, result=result)

        if ForeignWord.find(word):
            return dict(word=word , status=QueryStatus.foreign_word)

        result = PersianWord.add(word)

        transaction.commit()
        return dict(word=word , status=QueryStatus.success ,result=result)


    #@expose("parsidan.templates.contribution.submit_word_success")
    #@validate(SubmitWordForm, error_handler=submit_word_form)
    #def submit_word(self, word=None, translation=None, *args, **kwargs):
    #    return dict()

