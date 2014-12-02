# -*- coding: utf-8 -*-
__author__ = 'vahid'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
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


    def send(self, to=None, subject=None, body=None):
        message = MIMEMultipart('alternative')
        message.set_charset('utf8')
        message['FROM'] = self.sender


        # This solved the problem with the encode on the subject. #100
        message['Subject'] = Header(
            subject,
            'UTF-8'
        ).encode()

        message['To'] = to

        # And this on the body
        _attach = MIMEText(body, 'html', 'UTF-8')
        message.attach(_attach)

        session = smtplib.SMTP_SSL(self.host, port=self.port)
        session.login(self.username, self.password)
        try:
            session.sendmail(self.sender, to, message.as_string())
        finally:
            session.close()


    def send_template(self, to=None, subject=None, template=None, **kwargs):
        self.send(to=to, subject=subject, body=render(kwargs, template_name=template))

        # headers = self._get_headers(subject, to)
        # session = smtplib.SMTP_SSL(self.host, port=self.port)
        # session.login(self.username, self.password)
        # try:
        #     session.sendmail(self.sender, to, headers + "\r\n\r\n" + body)
        # finally:
        #     session.close()
