# -*- coding: utf-8 -*-
"""Parsidan Controller"""

from tg import expose, flash, request
from parsidan.model.dictionary import *
from parsidan.model import DBSession
from tg.controllers import RestController
from parsidan.controllers.error import ErrorController
from parsidan.controllers.secure import SecureController
from sqlalchemy import event

__all__ = ['DictionaryController']

secc = SecureController()


class DictionaryController(RestController):

    @expose('json')
    def getPersian (self , **kwargs):
        relatedWords = []
        words = []
        status=0
        v=None
        id = DBSession.query(Ar).filter(Ar.name == kwargs["word"]).first()

        if id:
            words = DBSession.query(Pe).filter(Pe.ar.any(id=id.id)).all()


        #if we cant find persian translate
        if not words:

            checkPe = DBSession.query(Pe).filter(Pe.name == kwargs['word']).count()
            if checkPe:
                #inserted word is a persian word !!!
                status=3
            else:
                # if not find any word we add the word in database to translate later

                checkAr = DBSession.query(Ar).filter(Ar.name == kwargs['word']).count()

                if checkAr:
                    status=2
                else:
                    word = Ar(name=kwargs['word'])

                try:
                    DBSession.add(word)

                except:
                    pass

                else:
                    #word successfully added
                    status=1



            # end adding
            #todo: find similar words
            #relatedWords = DBSession.query(Pe).filter( Pe.ar.any( id = id.id)).all()

        return dict(words=[word.name for word in words],status=status,relatedWords=[relword.name for relword in relatedWords])


    #while click on a persian word to view its alien equivalents
    @expose('json')
    def getAlien(self,**kwargs):
        words = []
        words = DBSession.query(Ar).filter( Ar.pe.any( id = kwargs['id'])).all()
        return dict(words=[(word.id , word.name) for word in words])


    #list of alien words which users search for its persian equivalent and no result was founded
    @expose('parsidan.templates.dictionary.alienList')


    def alienList(self):

        words = DBSession.query(Ar).filter(Ar.pe==None).all()
        print len(words)
        return dict(words = words)


    @expose('json')
    def assignPersian(self,**kwargs):
        success=0
        checkAr = DBSession.query(Ar).filter(Ar.id==kwargs['item']).first()

        if checkAr:
            checkPe = DBSession.query(Pe).filter(Pe.name==kwargs['word']).first()
            print 'arrrrrrrrrrrrrrr'



            try:
                if checkPe:
                    checkAr.pe.append(checkPe)

                else:
                    PeAdded=Pe(name=kwargs['word'])
                    checkAr.pe.append(PeAdded)

            except:
                success=0

            else:
                success = 1

        return dict( success = success)


    @expose('parsidan.templates.dictionary.myWords')
    def myWords(self):
        #todo: should be like bottom line which fetch user`s words not other`s
        #words = DBSession.query(Pe).join(Log).filter(Log.user==current_user.id,Log.action=='add').all()
        words = DBSession.query(Pe).all()
        return dict(words = words)




    @expose('json')
    def removeAlien(self,**kwargs):

        success=0
        pes = Pe.query.filter( Pe.id == kwargs['parentId']).one()
        ar =DBSession.query(Ar).filter(Ar.id == kwargs['id']).one()


        try:
            pes.ar.remove(ar);
        except:
            success=0

        return dict( success = success)


    @expose('json')
    def assignAlien(self,**kwargs):

        success=0
        checkPe = DBSession.query(Pe).filter(Pe.id==kwargs['item']).first()

        if checkPe:
            checkAr = DBSession.query(Ar).filter(Ar.name==kwargs['word']).first()

            print('++++++')

            if checkAr:
                checkPe.ar.append(checkAr)


            else:
                ArAdded=Ar(name=kwargs['word'])
                ArAdded=DBSession.add(ArAdded)
                checkPe.ar.append(ArAdded)

        return dict( success = success)



    @expose('json')
    def addPersian(self,**kwargs):
        words = Pe(name=kwargs['word'])
        DBSession.add(words)
        success=0
        try:
            DBSession.commit()
            success=words.id
        except:
            success = 2

        return dict( success = success)


def after_insert_listener(mapper, connection, target):
    # 'target' is the inserted object
    logAdd=Log(pe=target.id, action='add', user=request.identity.get('repoze.who.userid'))
    DBSession.add(logAdd)
    #DBSession.commit()


event.listen(Pe, 'after_insert', after_insert_listener)

