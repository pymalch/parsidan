# -*- coding: utf-8 -*-
__author__ = 'vahid'
from tg.i18n import lazy_ugettext as l_


class SecurityError(Exception):
    def __init__(self, msg=l_('Security Error')):
        super(SecurityError, self).__init__(msg)


class AuthenticationError(SecurityError):
    def __init__(self, msg=l_('Authentication Error')):
        super(AuthenticationError, self).__init__(msg)


class VerificationError(AuthenticationError):
    def __init__(self, msg=l_('Verification Error')):
        super(VerificationError, self).__init__(msg)
