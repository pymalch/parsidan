# -*- coding: utf-8 -*-
__author__ = 'vahid'

import tw2.bootstrap.forms as twf
import tw2.core as twc
import tg
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm, ReCaptchaValidator, FixedReCaptcha
from formencode.validators import FieldsMatch, String as StringValidator

class RegistrationForm(BaseForm):
    email = twf.TextField(label=l_('Email'), validator=twc.EmailValidator(required=True,msgs={'bademail':_('Must be a valid email address')}))
    nickname = twf.TextField(label=l_('Nickname'))
    password = twf.PasswordField(label=l_('Password'), validator=StringValidator(min=8, max=20))
    password_confirm = twf.PasswordField(label=l_('Password Confirm'), validator=twc.Required)
    recaptcha_challenge_field = twf.HiddenField()
    recaptcha_response_field = FixedReCaptcha(label=l_('Please Enter whatever you see in the below'),
                                                  public_key=tg.config.get('recaptcha.public_key'),
                                                  validator=ReCaptchaValidator(tg.config.get('recaptcha.private_key'),
                                                                               tg.config.get('domain.ip_address')))

    action = '/authentication/signup'
    submit = twf.SubmitButton(id='submit', value=l_('Sign Up'))
    validator = FieldsMatch('password', 'password_confirm')
