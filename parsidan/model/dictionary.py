__author__ = 'masoud'

from parsidan.model import DeclarativeBase, DBSession
from sqlalchemy import ForeignKey, Column, PrimaryKeyConstraint
from sqlalchemy.types import Unicode, Integer, Enum, DateTime, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import bindparam
from datetime import datetime
from parsidan.model.mixins import ConfirmableMixin, TimestampMixin


class QueryStatus:
    dictionary_not_found = 0
    dictionary_foreign_word = 1
    dictionary_persian_word = 2
    contribution_success_add = 3
    contribution_added_before = 4
    contribution_not_foreign_word = 5
    contribution_not_persian_word = 6

class PersianWord(TimestampMixin, ConfirmableMixin, DeclarativeBase):
    #TODO: Remove unnecessary spaces before inserting
    __tablename__ = "persian_word"

    id = Column(Integer,  primary_key=True)
    title = Column(Unicode(60), nullable=False, unique=True, index=True)
    alphabets = u"\u0622\u0627\u0628\u067E\u062A\u062B\u062C\u0686\u062D\u062E\u062F\u0630\u0631\u0632\u0633\u0634\u0635\u0636\u0637\u0638\u0639\u063A\u0641\u0642\u06A9\u06AF\u0644\u0645\u0646\u0648\u0647\u06CC"



    @classmethod
    def find(cls, title):
        return DBSession.query(cls).filter(cls.title==title).first()

    @classmethod
    def add(cls, title):
        if cls.find(title):
            return
        return DBSession.add(cls(title=title))

    @classmethod
    def list(cls, character=None, user=None):
        list = DBSession.query(cls)\
            .join(Dictionary)
        if character:
            list = list.filter( cls.title.startswith( '%s' % character ))
        if user:
            list = list.filter(Dictionary.user==user)
        return list.all()


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
    def add(cls, persianWord, foreignWord, user):
        return DBSession.add(Dictionary(foreign_word=foreignWord, persian_word=persianWord, status='confirmed', user=user))

    @classmethod
    def find(cls, persianWord, foreignWord):
        return DBSession.query(cls)\
            .filter(cls.persian_word_id== persianWord )\
            .filter(cls.foreign_word_id== foreignWord )\
            .first()

    @classmethod
    def query_persian(cls, expression):
        rate = cls.likes - cls.dislikes
        for r in DBSession.query(rate.label('rate'), PersianWord.title.label('title'))\
            .join(ForeignWord)\
            .join(PersianWord)\
            .filter(Dictionary.status == 'confirmed')\
            .filter(ForeignWord.title == expression)\
            .order_by(rate.desc()):

            yield r._asdict()


    @classmethod
    def query_foreign(cls, expression):
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

