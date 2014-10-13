# -*- coding: utf-8 -*-
__author__ = 'vahid'

import tw2.bootstrap.forms as twf
import tw2.core as twc
import tg
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm, ReCaptchaValidator, FixedReCaptcha
from formencode.validators import FieldsMatch

class RegistrationForm(BaseForm):
    email = twf.TextField(label=l_('Email'), validator=twc.EmailValidator)
    password = twf.PasswordField(label=l_('Password'))
    password_confirm = twf.PasswordField(label=l_('Password Confirm'))
    recaptcha_response_field = FixedReCaptcha(label=l_("Please Enter these words"),
                                                  public_key=tg.config.get('recaptcha.public_key'),
                                                  validator=ReCaptchaValidator(tg.config.get('recaptcha.private_key'),
                                                                               tg.config.get('domain.ip_address')))

    action = '/signup'
    submit = twf.SubmitButton(id='submit', value=l_('Login'))
    validator = FieldsMatch('password', 'password_confirm')