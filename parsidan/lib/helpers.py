# -*- coding: utf-8 -*-

"""WebHelpers used in parsidan."""

#from webhelpers import date, feedgenerator, html, number, misc, text
from markupsafe import Markup
from datetime import datetime
import tg.i18n


def current_year():
  now = datetime.now()
  return now.strftime('%Y')

def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)

def lang():
    langs =tg.i18n.get_lang(all=False)
    if langs:
        return langs[0]
    else:
        return None    

