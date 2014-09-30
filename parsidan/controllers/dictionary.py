# -*- coding: utf-8 -*-
"""Parsidan Controller"""

from tg import expose, flash
from parsidan.model.dictionary import *
from parsidan.model import DBSession
from tg.controllers import RestController
from parsidan.controllers.error import ErrorController

__all__ = ['DictionaryController']



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
                word = Ar(name=kwargs['word'])

                try:
                    v=DBSession.add(word)
                except:
                    #word added before (duplicate entry)
                    print('eeeee-------------------ee')
                    print(v)
                    status=2

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
    def persianAdd(self,**kwargs):
        success=0
        checkAr = DBSession.query(Ar).filter(Ar.id==kwargs['item']).first()

        if checkAr:
            checkPe = DBSession.query(Pe).filter(Pe.name==kwargs['word']).first()

            if checkPe:
                checkAr.pe.append(checkPe)

            else:
                PeAdded=Pe(name=kwargs['word'])
                checkAr.pe.append(PeAdded)

            try:
                DBSession.commit()
                success=1
            except:
                success=0

        return dict( success = success)


    @expose('parsidan.templates.dictionary.myWordsList')
    def dictionaryMyList(self):
        words = DBSession.query(Pe).join(Log).filter(Log.user==current_user.id,Log.action=='add').all()
        return dict(words = words)




'''






# Flask views





# Flask views
@expose('/nonPersian/delete',methods=['POST','GET'])
def nonPersianRemove():

    success=0
    pes = Pe.query.filter( Pe.id == request.form['parentId']).one()
    ar =DBSession.query(Ar).filter(Ar.id == request.form['id']).one()
    pes.ar.remove(ar);

    try:
        DBSession.commit()
        success=1
    except:
        success=0

    return jsonify( success = success)




# Flask views
@expose('/nonPersian/add',methods=['POST','GET'])
def nonPersianAdd():

    success=0
    checkPe = DBSession.query(Pe).filter(Pe.id==request.form['item']).first()

    if checkPe:
        checkAr = DBSession.query(Ar).filter(Ar.name==request.form['word']).first()

        if checkAr:
            checkPe.ar.append(checkAr)
            success=checkAr.id
        else:
            ArAdded=Ar(name=request.form['word'])
            checkPe.ar.append(ArAdded)

        try:
            DBSession.commit()
            success=ArAdded.id
        except:
            success=0

    return jsonify( success = success)



@expose('/persian/add',methods=['POST'])
def persianAdd():
    words = Pe(name=request.form['word'])
    DBSession.add(words)
    success=0
    try:
        DBSession.commit()
        success=words.id
    except:
        success = 2

    return str(success)



def after_insert_listener(mapper, connection, target):
    # 'target' is the inserted object
    from project.models.dictionary import Log
    from flask.ext.login import current_user
    logAdd=Log(pe=target.id, action='add', user=current_user.id)
    DBSession.add(logAdd)
    #DBSession.commit()


event.listen(Pe, 'after_insert', after_insert_listener)

'''