# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412228170.662082
_enable_loop = True
_template_filename = '/home/masoud/Desktop/parsidan/parsidan/templates/dictionary/main.mak'
_template_uri = '/home/masoud/Desktop/parsidan/parsidan/templates/dictionary/main.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'parsidan.templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n    <script type=text/javascript>\n        var word = Array();\n  $(function() {\n\n\n\n\n\n   $(\'#fromLangWrapper input\').keypress(function (e) {\n        var word = $(this).val();\n        if (e.which == 13) {\n            if (false || 0) {\n\n                return;\n            } else {\n                $(\'.messages .loading\').slideDown();\n                $.ajax({\n                    url: \'/dictionary/getPersian\',\n                    type: \'post\',\n                    data: { \'word\': word\n                    },\n                    success: function (data) {\n                       console.log(data);\n                        $(\'.messages .item\').slideUp();\n\n                        if(data.words.length){\n                            $(\'<div id="result" class="section"> </div>\').appendTo(\'#dictWrapper\');\n                            $.each(data.words,function(k,v){\n                                $(\'<span class="item">\' + v + \'<span class="like"><i class="fa fa-thumbs-up"></i><i class="fa fa-thumbs-down"></i></span></span>\').appendTo(\'#result\');\n                            });\n                        }else{\n\n                            $(\'.messages .noResult\').slideDown();\n                            $(\'.messages .s\'+data.status).slideDown();\n\n\n                        }\n\n                        if(data.relatedWords.length){\n                            $(\'<div id="relatedResult" class="section"> </div>\').appendTo(\'#dictWrapper\');\n                            $.each(data.relatedWords,function(k,v){\n                                $(\'<span class="item">\' + v + \'</span>\').appendTo(\'#relatedResult\');\n                            });\n                        }\n\n\n                    },\n                    error: function (xhr, status, error) {\n                        alert(\'')
        __M_writer(escape(_('Internal server error!')))
        __M_writer(u'\');\n                    },complete:function(){\n\n                        $(\'.messages .loading\').slideUp();\n                    }\n                });\n            }\n            e.preventDefault();\n            return;\n        }\n    });\n\n  });\n\n\n\n\n</script>\n\n <div id="dictWrapper" class="fs1">\n     <div id="fromLangWrapper">\n         <input type="text" class="form-control mainPersianInput" placeholder="')
        __M_writer(escape( _('Please enter non persian word') ))
        __M_writer(u'" >\n\n         <div class="messages">\n\n             <div class="loading"><img src="img/preloader.gif"> </div>\n            <span class="noResult item">')
        __M_writer(escape( _('Persian translate for this word did not find!') ))
        __M_writer(u'</span>\n            <span class="wordAdded s1 item"> ')
        __M_writer(escape( _('Word stores is database to translate later.') ))
        __M_writer(u'</span>\n            <span class="addedWordBefore s2 item">')
        __M_writer(escape( _('Word is already added and is waiting for translation.') ))
        __M_writer(u'</span>\n            <span class="aPersianWord s3 item">')
        __M_writer(escape( _('The word you entered is already a persian word!') ))
        __M_writer(u'</span>\n         </div>\n\n     </div>\n\n\n\n\n </div>\n         <div class="join">')
        __M_writer(escape( _("You can %(join)s and help us to improve this dictionary.") % {'join': "JOIN US" } ))
        __M_writer(u' </div>\n\n\n\n\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"33": 1, "34": 51, "35": 51, "36": 72, "37": 72, "38": 77, "39": 77, "40": 78, "41": 78, "42": 79, "43": 79, "44": 80, "45": 80, "46": 89, "47": 89, "53": 47, "27": 0}, "uri": "/home/masoud/Desktop/parsidan/parsidan/templates/dictionary/main.mak", "filename": "/home/masoud/Desktop/parsidan/parsidan/templates/dictionary/main.mak"}
__M_END_METADATA
"""
