# -*- coding: utf-8 -*-
__author__ = 'vahid'


#import tw2.forms as twf
import tw2.bootstrap.forms as twf
import tw2.core as twc
from parsidan.forms.base import BaseForm

class LoginForm(BaseForm):
    class child(twf.TableLayout):
        login = twf.TextField()
        password = twf.PasswordField()

    action = '/login_handler'