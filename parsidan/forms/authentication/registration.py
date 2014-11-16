# -*- coding: utf-8 -*-
__author__ = 'vahid'

import tw2.bootstrap.forms as twf
import tw2.core as twc
import tg
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm, ReCaptchaValidator, FixedReCaptcha
from parsidan.forms import validation_message


class RegistrationForm(BaseForm):
    email = twf.TextField(label=l_('Email'),
                          addon_icon={'right': 'glyphicon glyphicon-envelope'},
                          validator=twc.EmailValidator(required=True, msgs=validation_message))
    nickname = twf.TextField(label=l_('Nickname'),
                             addon_icon={'right': 'glyphicon glyphicon-flag'})
    password = twf.PasswordField(label=l_('Password'),
                                 addon_icon={'right': 'glyphicon glyphicon-lock'},
                                 validator=twc.LengthValidator(min=8, max=20, msgs=validation_message),
    )
    password_confirm = twf.PasswordField(label=l_('Password Confirm'),
                                         addon_icon={'right': 'glyphicon glyphicon-lock'},
                                         validator=twc.MatchValidator('password', msgs=validation_message),
    )
    recaptcha_challenge_field = twf.HiddenField()
    recaptcha_response_field = FixedReCaptcha(label=l_('Please Enter whatever you see in the below'),
                                              public_key=tg.config.get('recaptcha.public_key'),
                                              validator=ReCaptchaValidator(tg.config.get('recaptcha.private_key'),
                                                                           tg.config.get('domain.ip_address'),
                                                                           messages=validation_message
                                                                         ),
    )

    action = '/authentication/signup'
    submit = twf.SubmitButton(id='submit', value=l_('Sign Up'))