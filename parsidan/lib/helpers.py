# -*- coding: utf-8 -*-

"""WebHelpers used in parsidan."""

#from webhelpers import date, feedgenerator, html, number, misc, text
from markupsafe import Markup
from datetime import datetime
import tg
import urllib

debug = lambda: tg.config.get('debug')

def current_year():
  now = datetime.now()
  return now.strftime('%Y')

def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)

def lang():
    langs =tg.i18n.get_lang(all=False)
    if langs:
        return langs[0][:2]
    else:
        return None    

def url_quote(url):
    if isinstance(url, unicode):
        url = url.encode('utf8')
    return urllib.quote(url)