# -*- coding: utf-8 -*-
__author__ = 'vahid'

import tw2.bootstrap.forms as twf
import tw2.core as twc
import tg
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm, ReCaptchaValidator, FixedReCaptcha

class RegistrationForm(BaseForm):
    email = twf.TextField(label=l_('Email'),
                          validator=twc.EmailValidator(required=True,
                                                       msgs={'bademail':l_('Must be a valid email address')}))
    nickname = twf.TextField(label=l_('Nickname'))
    password = twf.PasswordField(label=l_('Password'), validator=twc.LengthValidator(min=8, max=20))
    password_confirm = twf.PasswordField(label=l_('Password Confirm'), validator=twc.MatchValidator('password_confirm'))
    recaptcha_challenge_field = twf.HiddenField()
    recaptcha_response_field = FixedReCaptcha(label=l_('Please Enter whatever you see in the below'),
                                                  public_key=tg.config.get('recaptcha.public_key'),
                                                  validator=ReCaptchaValidator(tg.config.get('recaptcha.private_key'),
                                                                               tg.config.get('domain.ip_address')))

    action = '/authentication/signup'
    submit = twf.SubmitButton(id='submit', value=l_('Sign Up'))