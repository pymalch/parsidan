# -*- coding: utf-8 -*-
__author__ = 'vahid'

import tw2.core as twc
import tw2.bootstrap.forms as twf
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm, ReCaptchaValidator, FixedReCaptcha
import tg

class RecoverPasswordForm(BaseForm):
    email = twf.TextField(label=l_('Email'),
                          validator=twc.EmailValidator(required=True,
                                                       msgs={'bademail':l_('Must be a valid email address')}))

    recaptcha_response_field = FixedReCaptcha(label=l_('Please Enter whatever you see in the below'),
                                                  public_key=tg.config.get('recaptcha.public_key'),
                                                  validator=ReCaptchaValidator(tg.config.get('recaptcha.private_key'),
                                                                               tg.config.get('domain.ip_address')))



    action = '/authentication/recover_password'
    submit = twf.SubmitButton(id='submit', value=l_('Send'))
