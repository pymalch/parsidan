# -*- coding: utf-8 -*-
__author__ = 'vahid'


import tw2.core as twc
#import tw2.forms as twf
import tw2.bootstrap.forms as twf

class LoginForm(twf.TableForm):
    # class child(twf.TableLayout):
    login = twf.TextField()
    password = twf.PasswordField()

    action = '/login_handler'