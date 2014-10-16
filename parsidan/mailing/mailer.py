# -*- coding: utf-8 -*-
__author__ = 'vahid'

import smtplib
from tg.render import render
import tg


class Mailer(object):
    def __init__(self):
        self.port = 465
        self.host = tg.config.get('mailing.smtp_server')
        self.username = tg.config.get('mailing.smtp_username')
        self.password = tg.config.get('mailing.smtp_password')
        self.sender = tg.config.get('mailing.from_address')

    def _get_headers(self, subject, to):
        return "\r\n".join(["From: " + self.sender,
                            "Subject: " + subject,
                            "To: " + to,
                            "MIME-Version: 1.0",
                            "Content-Type: text/html"])


    def send_template(self, to=None, subject=None, template=None, **kwargs):
        body = render(kwargs, template_name=template)

        headers = self._get_headers(subject, to)
        session = smtplib.SMTP_SSL(self.host, port=self.port)
        session.login(self.username, self.password)
        try:
            session.sendmail(self.sender, to, headers + "\r\n\r\n" + body)
        finally:
            session.close()
