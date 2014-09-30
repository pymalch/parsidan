# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1411888680.241833
_enable_loop = True
_template_filename = u'/home/masoud/Desktop/parsidan/parsidan/templates/master.mak'
_template_uri = u'/home/masoud/Desktop/parsidan/parsidan/templates/master.mak'
_source_encoding = 'utf-8'
from markupsafe import escape_silent as escape
_exports = ['footer', 'body_class', 'head_content', 'meta', 'title', 'main_menu', 'content_wrapper']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\n<html>\n<head>\n    ')
        __M_writer(escape(self.meta()))
        __M_writer(u'\n    <title>')
        __M_writer(escape(_('Parsidan')))
        __M_writer(u'</title>\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/bootstrap.min.css')))
        __M_writer(u'" />\n    <link rel="stylesheet" type="text/css" media="screen" href="')
        __M_writer(escape(tg.url('/css/style.css')))
        __M_writer(u'" />\n <script src="http://code.jquery.com/jquery.js"></script>    ')
        __M_writer(escape(self.head_content()))
        __M_writer(u'\n</head>\n<body class="')
        __M_writer(escape(self.body_class()))
        __M_writer(u'">\n    ')
        __M_writer(escape(self.main_menu()))
        __M_writer(u'\n  <div class="container">\n    ')
        __M_writer(escape(self.content_wrapper()))
        __M_writer(u'\n  </div>\n    ')
        __M_writer(escape(self.footer()))
        __M_writer(u'\n\n  <script src="')
        __M_writer(escape(tg.url('/javascript/bootstrap.min.js')))
        __M_writer(u'"></script>\n</body>\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  <footer class="footer hidden-xs hidden-sm">\n    <a class="pull-right" href="http://www.turbogears.org"><img style="vertical-align:middle;" src="')
        __M_writer(escape(tg.url('/img/under_the_hood_blue.png')))
        __M_writer(u'" alt="TurboGears 2" /></a>\n    <p>Copyright &copy; ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'TurboGears2')))
        __M_writer(u' ')
        __M_writer(escape(h.current_year()))
        __M_writer(u'</p>\n  </footer>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_class(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_content(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        response = context.get('response', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  <meta charset="')
        __M_writer(escape(response.charset))
        __M_writer(u'" />\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_main_menu(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        tmpl_context = context.get('tmpl_context', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        tg = context.get('tg', UNDEFINED)
        page = context.get('page', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  <!-- Navbar -->\n  <nav class="navbar navbar-default">\n    <div class="navbar-header">\n      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-content">\n        <span class="sr-only">Toggle navigation</span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n        <span class="icon-bar"></span>\n      </button>\n      <a class="navbar-brand" href="')
        __M_writer(escape(tg.url('/')))
        __M_writer(u'">\n        <img src="')
        __M_writer(escape(tg.url('/img/turbogears_logo.png')))
        __M_writer(u'" height="20" alt="TurboGears 2"/>\n        ')
        __M_writer(escape(getattr(tmpl_context, 'project_name', 'turbogears2')))
        __M_writer(u'\n      </a>\n    </div>\n\n    <div class="collapse navbar-collapse" id="navbar-content">\n      <ul class="nav navbar-nav">\n        <li class="')
        __M_writer(escape(('', 'active')[page=='index']))
        __M_writer(u'"><a href="')
        __M_writer(escape(tg.url('/')))
        __M_writer(u'">')
        __M_writer(escape(_('home')))
        __M_writer(u'</a></li>\n        <li class="')
        __M_writer(escape(('', 'active')[page=='about']))
        __M_writer(u'"><a href="')
        __M_writer(escape(tg.url('/dictionary/alienList')))
        __M_writer(u'">')
        __M_writer(escape(_('Make persian')))
        __M_writer(u'</a></li>\n\n      </ul>\n\n')
        if tg.auth_stack_enabled:
            __M_writer(u'      <ul class="nav navbar-nav navbar-right">\n')
            if not request.identity:
                __M_writer(u'        <li><a href="')
                __M_writer(escape(tg.url('/login')))
                __M_writer(u'">Login</a></li>\n')
            else:
                __M_writer(u'        <li><a href="')
                __M_writer(escape(tg.url('/logout_handler')))
                __M_writer(u'">Logout</a></li>\n        <li><a href="')
                __M_writer(escape(tg.url('/admin')))
                __M_writer(u'">Admin</a></li>\n')
            __M_writer(u'      </ul>\n')
        __M_writer(u'    </div>\n  </nav>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_wrapper(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        tg = context.get('tg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n  ')

        flash=tg.flash_obj.render('flash', use_js=False)
          
        
        __M_writer(u'\n')
        if flash:
            __M_writer(u'      <div class="row">\n        <div class="col-md-8 col-md-offset-2">\n              ')
            __M_writer(flash )
            __M_writer(u'\n        </div>\n      </div>\n')
        __M_writer(u'  ')
        __M_writer(escape(self.body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "24": 1, "25": 4, "26": 4, "27": 5, "28": 5, "29": 6, "30": 6, "31": 7, "32": 7, "33": 8, "34": 8, "35": 10, "36": 10, "37": 11, "38": 11, "39": 13, "40": 13, "41": 15, "42": 15, "43": 17, "44": 17, "45": 32, "46": 34, "47": 38, "48": 39, "49": 41, "50": 48, "51": 85, "57": 43, "65": 43, "66": 45, "67": 45, "68": 46, "69": 46, "70": 46, "71": 46, "77": 34, "86": 39, "95": 35, "100": 35, "101": 36, "102": 36, "108": 41, "112": 41, "118": 50, "128": 50, "129": 60, "130": 60, "131": 61, "132": 61, "133": 62, "134": 62, "135": 68, "136": 68, "137": 68, "138": 68, "139": 68, "140": 68, "141": 69, "142": 69, "143": 69, "144": 69, "145": 69, "146": 69, "147": 73, "148": 74, "149": 75, "150": 76, "151": 76, "152": 76, "153": 77, "154": 78, "155": 78, "156": 78, "157": 79, "158": 79, "159": 81, "160": 83, "166": 20, "172": 20, "173": 21, "177": 23, "178": 24, "179": 25, "180": 27, "181": 27, "182": 31, "183": 31, "184": 31, "190": 184}, "uri": "/home/masoud/Desktop/parsidan/parsidan/templates/master.mak", "filename": "/home/masoud/Desktop/parsidan/parsidan/templates/master.mak"}
__M_END_METADATA
"""
