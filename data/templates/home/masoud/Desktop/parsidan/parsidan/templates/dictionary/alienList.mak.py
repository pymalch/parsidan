# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1412228242.692949
_enable_loop = True
_template_filename = '/home/masoud/Desktop/parsidan/parsidan/templates/dictionary/alienList.mak'
_template_uri = '/home/masoud/Desktop/parsidan/parsidan/templates/dictionary/alienList.mak'
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
        tg = context.get('tg', UNDEFINED)
        words = context.get('words', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n\n\n')
        if not tg.auth_stack_enabled:
            __M_writer(u'    <script language="JavaScript">\n        $(function(){\n           $(\'#words .item\').click(function(){\n               if(!$(this).find(\'input\').length)\n                    $(\'<span class="input"><input type="text"><span class="fa fa-plus-circle"></span><span>\').appendTo($(this));\n                    $(this).find(\'input\').slideDown(100);\n           });\n\n               $(\'#words .item input\').live(\'keypress\',function (e) {\n                var title = $(this).val();\n                var div = $(this).parent().parent();\n\n                var item = div.attr(\'data-rel\');\n                if (e.which == 13) {\n                    alert(item);\n\n                        $.ajax({\n                            url: \'/translate/addPersian\',\n                            type: \'post\',\n                            data: { \'word\': title, \'item\': item\n                            },\n                            success: function (data) {\n\n                                if(data.success){\n                                    alert(\'success\');\n                                    $(\'<span class="pendingWord">\'+ title + \'</span>\').appendTo(div)\n                                    div.find(\'input\').val(\'\');\n                                }else{\n                                     alert(\'error adding\');\n\n                                }\n\n\n                                console.log(data);\n\n                            },\n                            error: function (xhr, status, error) {\n                                alert(\'error\');\n                            }\n                        });\n\n                    e.preventDefault();\n                    return;\n                }\n            });\n\n        });\n    </script>\n')
        __M_writer(u'\n')
        if words:
            __M_writer(u'\n    <div class="words listStyle1" id="words">\n')
            for word in words:
                __M_writer(u'            <div class="item" data-rel="')
                __M_writer(escape( word.id ))
                __M_writer(u'"><span class="word">')
                __M_writer(escape( word.name ))
                __M_writer(u'</span></div>\n')
            __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 1, "35": 5, "36": 6, "37": 55, "38": 56, "39": 57, "40": 59, "41": 60, "42": 60, "43": 60, "44": 60, "45": 60, "46": 62, "52": 46, "27": 0}, "uri": "/home/masoud/Desktop/parsidan/parsidan/templates/dictionary/alienList.mak", "filename": "/home/masoud/Desktop/parsidan/parsidan/templates/dictionary/alienList.mak"}
__M_END_METADATA
"""
