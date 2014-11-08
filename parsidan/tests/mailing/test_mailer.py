# -*- coding: utf-8 -*-
__author__ = 'vahid'

from nose.tools import eq_, ok_
from unittest import TestCase
from parsidan.tests import TestController
from parsidan.mailing import Mailer


class TestAuthentication(TestController):

     application_under_test = 'main'

     def test_mailer(self):
        m = Mailer()
        m.send(
            to="website@parsidan.com",
            subject=u'آزمایش',
            body="Test Email, آزمایش")
