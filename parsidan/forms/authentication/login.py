# -*- coding: utf-8 -*-
__author__ = 'vahid'



import tw2.bootstrap.forms as twf
import tw2.core as twc
import tg
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm, ReCaptchaValidator, FixedReCaptcha


class LoginForm(BaseForm):
    login = twf.TextField(label=l_('Email'))
    password = twf.PasswordField(label=l_('Password'))
    # recaptcha_response_field = FixedReCaptcha(label=l_("Please Enter these words"),
    #                                               public_key=tg.config.get('recaptcha.public_key'),
    #                                               validator=ReCaptchaValidator(tg.config.get('recaptcha.private_key'),
    #                                                                            tg.config.get('domain.ip_address')))

    action = '/login_handler'
    submit = twf.SubmitButton(id='submit', value=l_('Login'))