__author__ = 'masoud'

from parsidan.model import DeclarativeBase, DBSession
from sqlalchemy import ForeignKey, Column, PrimaryKeyConstraint
from sqlalchemy.types import Unicode, Integer, Enum, DateTime, BigInteger
from sqlalchemy.orm import relationship
from datetime import datetime

class TimestampMixin(object):
    entry_time = Column(DateTime, default=datetime.now)


class ConfirmableMixin(object):
    status = Column(Enum('pending', 'confirmed', name="foreign_word_status"), default='pending', nullable=True)

    def confirm(self):
        self.status = 'confirmed'


class PersianWord(TimestampMixin, ConfirmableMixin, DeclarativeBase):
    #TODO: Remove unnecessary spaces before inserting
    __tablename__ = "persian_word"

    id = Column(Integer,  primary_key=True)
    title = Column(Unicode(60), nullable=False, unique=True, index=True)


class ForeignWord(TimestampMixin, ConfirmableMixin, DeclarativeBase):
    #TODO: Remove unnecessary spaces before inserting
    __tablename__ = "foreign_word"

    id = Column(Integer,  primary_key=True)
    title = Column(Unicode(50), nullable=False , unique=True, index=True )
    hits = Column(BigInteger, default=0, nullable=False)


class Dictionary(TimestampMixin, ConfirmableMixin, DeclarativeBase):
    __tablename__ = "dictionary"
    __table_args__ = (
        PrimaryKeyConstraint("foreign_word_id", "persian_word_id", name="dictionary_pk"),
    )

    foreign_word_id = Column(Integer, ForeignKey('foreign_word.id'), nullable=False, primary_key=True)
    foreign_word = relationship("ForeignWord")

    persian_word_id = Column(Integer, ForeignKey('persian_word.id'), nullable=False, primary_key=True)
    persian_word = relationship("PersianWord")

    likes = Column(Integer, nullable=False, default=0)
    dislikes = Column(Integer, nullable=False, default=0)

    @classmethod
    def query(cls, expression):
        rate = cls.likes - cls.dislikes
        for r in DBSession.query(rate.label('rate'), PersianWord.title.label('offer'))\
            .join(ForeignWord)\
            .join(PersianWord)\
            .filter(Dictionary.status == 'confirmed')\
            .filter(ForeignWord.title == expression)\
            .order_by(rate.desc()):

            yield r._asdict()


# class ActivityLog(DeclarativeBase):
#     __tablename__ = "activity_log"
#
#     id = Column("id", Integer, primary_key=True)
#     pe = Column("pe" , Integer(), ForeignKey('dic_pe.id'),default=None , index=True)
#     user = Column('user', Integer(), ForeignKey('tg_user.user_id', ondelete='CASCADE'))
#     action = Column("action" , String(50), default=None , index=True)
#     datetime = Column('datetime',DateTime, default=datetime.now )

