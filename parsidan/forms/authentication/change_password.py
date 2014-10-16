# -*- coding: utf-8 -*-
__author__ = 'vahid'

import tw2.bootstrap.forms as twf
from tg.i18n import lazy_ugettext as l_
from parsidan.widgets import BaseForm
from formencode.validators import FieldsMatch, String as StringValidator

class ChangePasswordForm(BaseForm):
    current_password = twf.PasswordField(label=l_('Current Password'), validator=StringValidator(min=8, max=20))
    new_password = twf.PasswordField(label=l_('New Password'), validator=StringValidator(min=8, max=20))
    password_confirm = twf.PasswordField(label=l_('New Password'), validator=StringValidator(min=8, max=20))

    validator = FieldsMatch('new_password', 'password_confirm')

    action = '/authentication/change_password'
    submit = twf.SubmitButton(id='submit', value=l_('Change'))
