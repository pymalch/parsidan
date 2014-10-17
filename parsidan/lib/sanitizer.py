# -*- coding: utf-8 -*-


__author__ = 'vahid'


__mappings = {
    u'\u0643': u'\u06A9',
    u'\u06AB': u'\u06A9',
    u'\u06AA': u'\u06A9',

    u'\u064A': u'\u06CC',
    u'\u0649': u'\u06CC',
    u'\u06CD': u'\u06CC',
    u'\u06CE': u'\u06CC',
    u'\u06D3': u'\u06CC',
    u'\u06D2': u'\u06CC',
    u'\u06D1': u'\u06CC',
    u'\u06D0': u'\u06CC',

    #u'\u0020': u'\u00A0',


}

def sanitize(word):
    if not isinstance(word, unicode):
        word = word.decode('utf8')
    result = u''
    for c in word.strip():
        if c in __mappings:
            result += __mappings[c]
        else:
            result += c
    return result