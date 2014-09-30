# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1411285951.72868
_enable_loop = True
_template_filename = '/home/masoud/Desktop/parsidan/parsidan/templates/environ.mak'
_template_uri = '/home/masoud/Desktop/parsidan/parsidan/templates/environ.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['head_content', 'title']


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
    return runtime._inherit_from(context, u'local:templates.master', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        environment = context.get('environment', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n  <div class="row">\n    <div class="col-xs-12">\n      <h2>The WSGI nature of the framework</h2>\n\n      <p>In this page you can see all the WSGI variables your request object has,\n         the ones in capital letters are required by the spec, then a sorted by\n         component list of variables provided by the Components, and at last\n         the "wsgi." namespace with very useful information about your WSGI Server</p>\n      <p>The keys in the environment are:</p>\n\n      <div class="table-responsive">\n        <table class="table table-hover">\n')
        for key in sorted(environment):
            __M_writer(u'          <tr>\n              <td>')
            __M_writer(escape(key))
            __M_writer(u'</td>\n              <td>')
            __M_writer(escape(environment[key]))
            __M_writer(u'</td>\n          </tr>\n')
        __M_writer(u'        </table>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n  <style>\n    .table {\n      word-wrap: break-word;\n      table-layout: fixed;\n    }\n  </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n  Learning TurboGears 2.3: Information about TG and WSGI\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"34": 1, "35": 5, "36": 14, "37": 28, "38": 29, "39": 30, "40": 30, "41": 31, "42": 31, "43": 34, "49": 7, "53": 7, "59": 3, "27": 0, "69": 63, "63": 3}, "uri": "/home/masoud/Desktop/parsidan/parsidan/templates/environ.mak", "filename": "/home/masoud/Desktop/parsidan/parsidan/templates/environ.mak"}
__M_END_METADATA
"""
