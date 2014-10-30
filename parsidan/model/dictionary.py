__author__ = 'masoud'

from parsidan.model import DeclarativeBase, DBSession
from sqlalchemy import ForeignKey, Column, PrimaryKeyConstraint
from sqlalchemy.types import Unicode, Integer, Enum, DateTime, BigInteger
from sqlalchemy.orm import relationship
from datetime import datetime
from parsidan.model.mixins import ConfirmableMixin, TimestampMixin


class PersianWord(TimestampMixin, ConfirmableMixin, DeclarativeBase):
    #TODO: Remove unnecessary spaces before inserting
    __tablename__ = "persian_word"

    id = Column(Integer,  primary_key=True)
    title = Column(Unicode(60), nullable=False, unique=True, index=True)


    @classmethod
    def find(cls, title):
        return DBSession.query(cls).filter(cls.title==title).first()

    @classmethod
    def add(cls, title):
        if cls.find(title):
            return
        return DBSession.add(cls(title=title))

    @classmethod
    def list(cls, user):
        return DBSession.query(cls)\
            .join(Dictionary)\
            .filter(Dictionary.user==user).all()


class ForeignWord(TimestampMixin, ConfirmableMixin, DeclarativeBase):
    #TODO: Remove unnecessary spaces before inserting
    __tablename__ = "foreign_word"

    id = Column(Integer,  primary_key=True)
    title = Column(Unicode(50), nullable=False , unique=True, index=True )
    hits = Column(BigInteger, default=0, nullable=False)

    @classmethod
    def find(cls, title):
        return DBSession.query(cls).filter(cls.title==title).first()

    @classmethod
    def hit(cls, title):
        word = cls.find(title)
        word.hits += 1
        return word

    @classmethod
    def check_and_hit(cls, title):
        word = cls.find(title)
        if word:
            word.hits += 1
        else:
            word = cls(title=title)
            DBSession.add(word)
        return word

class Dictionary(TimestampMixin, ConfirmableMixin, DeclarativeBase):
    __tablename__ = "dictionary"
    __table_args__ = (
        PrimaryKeyConstraint("foreign_word_id", "persian_word_id", name="dictionary_pk"),
    )

    foreign_word_id = Column(Integer, ForeignKey('foreign_word.id'), nullable=False, primary_key=True)
    foreign_word = relationship("ForeignWord")

    persian_word_id = Column(Integer, ForeignKey('persian_word.id'), nullable=False, primary_key=True)
    persian_word = relationship("PersianWord")

    user =  Column(Integer, ForeignKey('user.id'), nullable=False, index=True)

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


    @classmethod
    def find_persian_equivalents(cls, expression):
        rate = cls.likes - cls.dislikes
        for r in DBSession.query(rate.label('rate'), ForeignWord.title.label('title'))\
            .join(ForeignWord)\
            .join(PersianWord)\
            .filter(PersianWord.title == expression)\
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

