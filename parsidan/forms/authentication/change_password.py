# -*- coding: utf-8 -*-
__author__ = 'vahid'

import tw2.bootstrap.forms as twf
import tw2.core as twc
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm
from parsidan.forms import validation_message

from formencode.validators import FieldsMatch

class ChangePasswordForm(BaseForm):
    current_password = twf.PasswordField(label=l_('Current Password'), validator=twc.StringLengthValidator(required=True ,min=8, max=20, msgs=validation_message))
    new_password = twf.PasswordField(label=l_('New Password'), validator=twc.StringLengthValidator(required=True, min=8, max=20, msgs=validation_message))
    password_confirm = twf.PasswordField(label=l_('New Password'), validator=twc.StringLengthValidator(required=True, min=8, max=20, msgs=validation_message))

    validator = FieldsMatch('new_password', 'password_confirm')

    action = '/authentication/change_password'
    submit = twf.SubmitButton(id='submit', value=l_('Change'))
