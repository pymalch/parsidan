# -*- coding: utf-8 -*-
__author__ = 'vahid'
import tw2.core as twc
import tw2.bootstrap.forms as twf


class BaseForm(twf.BootstrapForm):
    child = twc.Variable(default=twf.FormGroupLayout)

