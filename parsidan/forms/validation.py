# -*- coding: utf-8 -*-
__author__ = 'vahid'

from tg.i18n import lazy_ugettext as l_

messages = {
    'string_tooshort': l_('Please enter at lease %s characters.') % 8,
    'string_toolong': l_('The maximum characters allowed are %s.') % 20,
    'required': l_('Enter a value'),
    'bademail':l_('Must be a valid email address'),
    'mismatch' :l_('Must match Password')

}
