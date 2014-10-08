# -*- coding: utf-8 -*-
"""Setup the parsidan application"""
from __future__ import print_function

import logging
from tg import config
from parsidan import model
import transaction

def bootstrap(command, conf, vars):
    """Place any commands to setup parsidan here"""

    # <websetup.bootstrap.before.auth>
    from sqlalchemy.exc import IntegrityError
    try:
        u = model.User()
        u.user_name = u'manager'
        u.display_name = u'Example manager'
        u.email_address = u'manager@somedomain.com'
        u.password = u'managepass'
    
        model.DBSession.add(u)
    
        g = model.Group()
        g.group_name = u'managers'
        g.display_name = u'Managers Group'
    
        g.users.append(u)
    
        model.DBSession.add(g)
    
        p = model.Permission()
        p.permission_name = u'manage'
        p.description = u'This permission give an administrative right to the bearer'
        p.groups.append(g)
    
        model.DBSession.add(p)
    
        u1 = model.User()
        u1.user_name = u'editor'
        u1.display_name = u'Example editor'
        u1.email_address = u'editor@somedomain.com'
        u1.password = u'editpass'
    
        model.DBSession.add(u1)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your auth data, it may have already been added:')
        import traceback
        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')

    # <websetup.bootstrap.after.auth>


    # <websetup.bootstrap.before.dictionary>
    from sqlalchemy.exc import IntegrityError
    try:

        salam = model.ForeignWord(title=u'سلام', status='confirmed')
        hi = model.ForeignWord(title=u'hi', status='confirmed')
        dorood = model.PersianWord(title=u'درود')
        dorood_bar_shoma = model.PersianWord(title=u'درود بر شما')

        model.DBSession.add(model.Dictionary(foreign_word=salam, persian_word=dorood, likes=10, dislikes=3, status='confirmed'))
        model.DBSession.add(model.Dictionary(foreign_word=salam, persian_word=dorood_bar_shoma, likes=5, dislikes=3, status='confirmed'))
        model.DBSession.add(model.Dictionary(foreign_word=hi, persian_word=dorood, likes=12, dislikes=4, status='confirmed'))
        model.DBSession.add(model.Dictionary(foreign_word=hi, persian_word=dorood_bar_shoma, likes=5, dislikes=3, status='confirmed'))


        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your dictionary data, it may have already been added:')
        import traceback
        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')

    # <websetup.bootstrap.after.dictionary>