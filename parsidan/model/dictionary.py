__author__ = 'masoud'

from parsidan.model import DeclarativeBase, metadata, DBSession
from parsidan.model.auth import User
from datetime import datetime

from sqlalchemy import Table, ForeignKey, Column, PrimaryKeyConstraint
from sqlalchemy.types import Unicode, Integer, DateTime, String
from sqlalchemy.types import Unicode, Integer, DateTime, String, SMALLINT
from sqlalchemy.orm import relationship, backref

ar_pe = Table(
    "dic_rel_ar_pe",
    metadata,
    Column("pe", Integer, ForeignKey("dic_pe.id"),primary_key=True),
    Column("ar", Integer, ForeignKey("dic_ar.id"),primary_key=True),
    PrimaryKeyConstraint('pe', 'ar'),

)
'''
class Ar_pe(object):

    def __init__(self, pe=None, ar=None):
        self.pe = pe
        self.ar = ar

mapper(Ar_pe, ar_pe)

'''
class Pe(DeclarativeBase):
    __tablename__ = "dic_pe"


    id = Column("id", Integer,  primary_key=True)
    name = Column("name", Unicode(50), nullable=False, unique=True )
    like = Column("like" , Integer, default=None )
    dislike = Column("dislike" , Integer, default=None )
    status = Column("status" , SMALLINT, default=None, index=True)



    ar = relationship('Ar', secondary=ar_pe,
        backref=backref('dic_pe', lazy='dynamic'),cascade="all, delete")





class Ar(DeclarativeBase):
    __tablename__ = "dic_ar"

    id = Column("id", Integer,  primary_key=True)
    name = Column("name", Unicode(50), nullable=False , unique=True)
    status = Column("status" , SMALLINT, default=None , index=True)
    pe = relationship('Pe', secondary=ar_pe,
        backref=backref('dic_ar', lazy='dynamic'),cascade="all, delete")



class Log(DeclarativeBase):
    __tablename__ = "dic_log"

    id = Column("id", Integer, primary_key=True)
    pe = Column("pe" , Integer(), ForeignKey('dic_pe.id'),default=None , index=True)
    user = Column('user', Integer(), ForeignKey('tg_user.user_id', ondelete='CASCADE'))
    action = Column("action" , String(50), default=None , index=True)
    datetime = Column('datetime',DateTime, default=datetime.now )


#todo





__all__ = ['Ar','Pe','ar_pe','Log']

