# -*- coding: utf-8 -*-
__author__ = 'vahid'
from sqlalchemy import Column
from sqlalchemy.types import Enum, DateTime
from datetime import datetime


class TimestampMixin(object):
    entry_time = Column(DateTime, default=datetime.now)


class ConfirmableMixin(object):
    status = Column(Enum('pending', 'confirmed', name="foreign_word_status"), default='pending', nullable=True)

    def confirm(self):
        self.status = 'confirmed'
