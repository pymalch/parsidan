# -*- coding: utf-8 -*-
__author__ = 'vahid'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension
import transaction

engine = create_engine('sqlite:///practice_data.db', echo=True)
DeclarativeBase = declarative_base()
Session = sessionmaker(autoflush=True, autocommit=False, bind=engine,
                      extension=ZopeTransactionExtension())


class User(DeclarativeBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

DeclarativeBase.metadata.create_all(engine)

if __name__ == '__main__':
    session = Session()
    ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

    session.add(ed_user)
    session.flush()
    #session.commit()
    #transaction.commit()

    print ed_user.id

