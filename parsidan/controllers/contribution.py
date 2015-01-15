# -*- coding: utf-8 -*-

from tg import expose, flash, url, lurl, request, redirect, require
from tg.i18n import ugettext as _, lazy_ugettext as l_
from parsidan.model import User,PersianWord, ForeignWord, Dictionary, QueryStatus
from parsidan.forms.contribution import SubmitWordForm
from tg.decorators import validate
from parsidan.lib.base import BaseController
import transaction
from tg.predicates import not_anonymous
from parsidan.lib.sanitizer import sanitize
from tgext.crud import EasyCrudRestController
__author__ = 'vahid'

__all__ = ['ContributionController']



class ContributionController(BaseController):

    allow_only = not_anonymous(msg=l_('Please login to view this page.'))

    @expose("parsidan.templates.contribution.index")
    def index(self):
        return dict()

    @expose("parsidan.templates.contribution.manage")
    def manage(self, type= None):

        if type == 'persian':
            words = PersianWord.get_pending()

        elif type == 'foreign':
            words = ForeignWord.get_pending()

        else:
            words = Dictionary.get_pending()

        return dict(words=words, type=type)

    @expose("json")
    def submit_persian_word(self, word, sourceWord):

        #word is a persian one
        word = sanitize(word)
        #sourceord is the foreign one
        sourceWord = sanitize(sourceWord)

        import time
        time.sleep(1)
        if ForeignWord.find(word):
            return dict(word=word , status=QueryStatus.contribution_not_persian_word)

        persianWord = PersianWord.find(word)
        foreignWord = ForeignWord.find(sourceWord)
        if persianWord and foreignWord:
            if Dictionary.find(persianWord.id, foreignWord.id):
                return dict(word=word , status=QueryStatus.contribution_added_before)
        if not persianWord:
            persianWord= PersianWord(title=word)
        if not foreignWord:
            foreignWord = ForeignWord(title=sourceWord)

        Dictionary.add(persianWord, foreignWord,  request.identity['user'].id)

        result = transaction.commit()
        return dict(word=word , status=QueryStatus.contribution_success_add,result=result)

    @expose("json")
    def submit_foreign_word(self, word, sourceWord):

        #word must be a foreign word
        word = sanitize(word)

        #sourceWord must be a persian word
        sourceWord = sanitize(sourceWord)

        import time
        time.sleep(1)
        if PersianWord.find(word):
            return dict(word=word , status=QueryStatus.contribution_not_foreign_word)

        foreignWord = ForeignWord.find(word)
        persianWord = PersianWord.find(sourceWord)

        if persianWord and foreignWord:
            if Dictionary.find(persianWord.id, foreignWord.id):
                return dict(word=word , status=QueryStatus.contribution_added_before)
        if not persianWord:
            persianWord= PersianWord(title=sourceWord)
        if not foreignWord:
            foreignWord = ForeignWord(title=word)

        Dictionary.add(persianWord, foreignWord,  request.identity['user'].id)

        result = transaction.commit()
        return dict(word=word , status=QueryStatus.contribution_success_add,result=result)


