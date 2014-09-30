# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1411274293.719571
_enable_loop = True
_template_filename = '/home/masoud/Desktop/parsidan/parsidan/templates/login.mak'
_template_uri = '/home/masoud/Desktop/parsidan/parsidan/templates/login.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['title']


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
        tg = context.get('tg', UNDEFINED)
        login_counter = context.get('login_counter', UNDEFINED)
        came_from = context.get('came_from', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n  <h1>Login</h1>\n\n  <div class="row">\n    <div class="col-md-8 col-md-offset-1">\n      <form action="')
        __M_writer(escape(tg.url('/login_handler', params=dict(came_from=came_from, __logins=login_counter))))
        __M_writer(u'"\n            method="post" accept-charset="UTF-8" class="form-horizontal">\n        <div class="form-group">\n          <label class="col-sm-2 control-label">Username:</label>\n          <div class="col-sm-10">\n            <input class="form-control" type="text" name="login"/>\n          </div>\n        </div>\n        <div class="form-group">\n          <label class="col-sm-2 control-label">Password:</label>\n          <div class="col-sm-10">\n            <input class="form-control" type="password" name="password"/>\n          </div>\n        </div>\n        <div class="form-group">\n          <div class="col-sm-10 col-sm-offset-2">\n            <div class="checkbox">\n              <label>\n                <input type="checkbox" name="remember" value="2252000" /> remember me\n              </label>\n            </div>\n          </div>\n        </div>\n        <div class="form-group">\n          <div class="col-sm-10 col-sm-offset-2">\n            <button type="submit" class="btn btn-default">Login</button>\n          </div>\n        </div>\n      </form>\n    </div>\n  </div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'Login Form')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"36": 1, "37": 2, "38": 7, "39": 7, "45": 2, "49": 2, "55": 49, "27": 0}, "uri": "/home/masoud/Desktop/parsidan/parsidan/templates/login.mak", "filename": "/home/masoud/Desktop/parsidan/parsidan/templates/login.mak"}
__M_END_METADATA
"""
