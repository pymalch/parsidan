# -*- coding: utf-8 -*-
__author__ = 'vahid'


from tw2.recaptcha import ReCaptchaWidget
from tw2.recaptcha.validator import ReCaptchaValidator as BadReCaptchaValidator

class FixedReCaptcha(ReCaptchaWidget):
    """
    Hack by Vahid Mardani, due the tw2.recaptcha validation bug
    """
    _sub_compound = True
    pass

class ReCaptchaValidator(BadReCaptchaValidator):
    """
    Hack by Vahid Mardani, due the tw2.recaptcha validation bug
    """
    not_empty = True