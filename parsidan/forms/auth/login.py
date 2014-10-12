# -*- coding: utf-8 -*-
__author__ = 'vahid'


#import tw2.forms as twf
import tw2.bootstrap.forms as twf
import tw2.core as twc
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm


class LoginForm(BaseForm):
    login = twf.TextField(label=l_('Username'))
    password = twf.PasswordField(label=l_('Password'))

    action = '/login_handler'