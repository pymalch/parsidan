# -*- coding: utf-8 -*-

from tg import expose, flash, url, lurl, request, redirect, require
from tg.i18n import ugettext as _, lazy_ugettext as l_
from parsidan.model import User
from parsidan.forms.contribution import SubmitWordForm
from tg.decorators import validate
from parsidan.lib.base import BaseController
import transaction
from tg.predicates import not_anonymous
__author__ = 'vahid'

__all__ = ['ContributionController']

class ContributionController(BaseController):

    allow_only = not_anonymous(msg=l_('Please login to view this page.'))

    @expose("parsidan.templates.contribution.index")
    def index(self):
        return dict()


    @expose("parsidan.templates.contribution.submit_word")
    def submit_word_form(self, *args, **kwargs):
        form = SubmitWordForm.reg()
        return dict(form=form)

    @expose("parsidan.templates.contribution.submit_word_success")
    @validate(SubmitWordForm, error_handler=submit_word_form)
    def submit_word(self, word=None, translation=None, *args, **kwargs):
        return dict()

