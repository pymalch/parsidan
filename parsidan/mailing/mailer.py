# -*- coding: utf-8 -*-
__author__ = 'vahid'

import smtplib
from tg import render


class Mailer(object):
    def __init__(self):
        self.host = config.get('mailing.smtp_server')
        self.username = config.get('mailing.smtp_username')
        self.password = config.get('mailing.smtp_password')
        self.sender = config.get('mailing.from')

    def _get_headers(self, subject, to):
        return "\r\n".join(["From: " + self.sender,
                            "Subject: " + subject,
                            "To: " + to,
                            "MIME-Version: 1.0",
                            "Content-Type: text/html"])


    def send_template(self, to=None, subject=None, template=None, **kwargs):
        body = render(kwargs, template_name=template)

        headers = self._get_headers(subject, )
        session = smtplib.SMTP_SSL(self.host)
        session.login(self.username, self.password)
        try:
            session.sendmail(self.sender, self.to, headers + "\r\n\r\n" + body)
        finally:
            session.close()
