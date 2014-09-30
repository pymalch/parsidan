# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1411156630.796907
_enable_loop = True
_template_filename = '/home/masoud/Desktop/parsidan/parsidan/templates/about.mak'
_template_uri = '/home/masoud/Desktop/parsidan/parsidan/templates/about.mak'
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
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        __M_writer(u'\n\n    <div class="row">\n      <div class="col-md-12">\n        <div class="page-header">\n          <h2>Architectural basics of a quickstart TG2 site.</h2>\n        </div>\n\n        <p>The TG2 quickstart command produces this basic TG site. Here\'s how it works.</p>\n      </div>\n    </div>\n\n    <div class="row">\n      <div class="col-md-4">\n        <div class="well">\n          <ul class="nav nav-list">\n            <li class="nav-header">About Architecture</li>\n            <li><a href="#data-model">Data Model</a></li>\n            <li><a href="#url-structure">URL Structure</a></li>\n            <li><a href="#template-reuse">Templates</a></li>\n')
        if tg.auth_stack_enabled:
            __M_writer(u'            <li class="nav-header">Authentication</li>\n            <li><a href="#authentication">Authorization and Authentication</a></li>\n')
        __M_writer(u'          </ul>\n        </div>\n\n        <div class="well" id="data-model">\n          <h3>Code my data model</h3>\n\n          <p>When you want a model for storing favorite links or wiki content, the\n          <code>/model</code> folder in your site is ready to go.</p>\n\n          <p>You can build a dynamic site without any data model at all. There still be a\n          default data-model template for you if you didn\'t enable authentication and\n          authorization in quickstart. If you have enabled authorization, the auth\n          data-model is ready-made.</p>\n        </div>\n\n        <div class="well" id="url-structure">\n          <h3>Design my URL structure</h3>\n\n          <p>The "<code>root.py</code>" file under the <code>/controllers</code> folder has\n          your URLs. When you called this url (<code><a href=\n          "')
        __M_writer(escape(tg.url('/about')))
        __M_writer(u'">about</a></code>), the command went through the\n          RootController class to the <code>about()</code> method.</p>\n\n          <p>Those Python methods are responsible to create the dictionary of variables\n          that will be used in your web views (template).</p>\n        </div>\n\n        <div class="well" id="template-reuse">\n            <h3>Reuse the web page elements</h3>\n\n            <p>A web page viewed by user could be constructed by single or several reusable\n                templates under <code>/templates</code>.\n                Each projects gets quickstarted with a <strong><span class="label label-info">master.html</span></strong>\n                template and a bunch of templates for the pages provided by the RootController.\n            </p>\n        </div>\n      </div>\n\n      <div class="col-md-8">\n        <img src="http://www.turbogears.org/2.1/docs/_images/tg2_files.jpg"\n             alt="TurboGears2 quickstarted project" />\n      </div>\n    </div>\n\n    <div class="row">\n      <div class="col-md-12">\n        <h3>The Master Template</h3>\n\n        <p>The <strong><span class="label label-info">master.html</span></strong> template\n        controls the overall design of the page we\'re looking at. It draws the headers,\n        the footer, the notices flash and embeds the content of each page of your web applications.\n        Thus the "master.html" template provides the overall architecture for\n        each page in this site.</p>\n\n        <p>There\'s more to the "master.html" template... study it to see how the\n        &lt;title&gt; tags and static JS and CSS files are brought into the page.\n        Templating with Genshi is a powerful tool and we\'ve only scratched the surface.\n        There are also a few little CSS tricks hidden in these pages, like the use of a\n        "clearingdiv" to make sure that your footer stays below the sidebars and always\n        looks right. That\'s not TG2 at work, just CSS. You\'ll need all your skills to\n        build a fine web app, but TG2 will make the hard parts easier so that you can\n        concentrate more on good design and content rather than struggling with\n        mechanics.</p>\n      </div>\n    </div>\n\n')
        if tg.auth_stack_enabled:
            __M_writer(u'    <div class="row">\n      <div class="col-md-12" id="authentication" >\n        <h3>Authentication &amp; Authorization in a TG2 site.</h3>\n\n        <p>If you have access to this page, this means you have enabled authentication\n        and authorization in the quickstart to create your project.</p>\n\n        <p>The gearbox command will have created a few specific controllers for you. But\n        before you go to play with those controllers you\'ll need to make sure your\n        application has been properly bootstapped. This is dead easy, here is how to do\n        this:</p>\n        <pre>gearbox setup-app</pre>\n\n        <p>inside your application\'s folder and you\'ll get a database setup (using the\n        preferences you have set in your development.ini file). This database will also\n        have been prepopulated with some default logins/passwords so that you can test\n        the secured controllers and methods.</p>\n\n        <p>To change the comportement of this setup-app command you just need to edit\n        the <code>websetup.py</code> file.</p>\n\n        <p>Now try to visiting the <a href=\n        "')
            __M_writer(escape(tg.url('/manage_permission_only')))
            __M_writer(u'">manage_permission_only</a> URL. You will\n        be challenged with a login/password form.</p>\n\n        <p>Only managers are authorized to visit this method. You will need to log-in\n        using:</p>\n        <pre>login: manager\npassword: managepass</pre>\n\n        <p>Another protected resource is <a href=\n        "')
            __M_writer(escape(tg.url('/editor_user_only')))
            __M_writer(u'">editor_user_only</a>. This one is protected by\n        a different set of permissions. You will need to be <code>editor</code> with a\n        password of <code>editpass</code> to be able to access it.</p>\n\n        <p>The last kind of protected resource in this quickstarted app is a full so\n        called <a href="')
            __M_writer(escape(tg.url('/secc')))
            __M_writer(u'">secure controller</a>. This controller is\n        protected globally. Instead of having a @require decorator on each method, we\n        have set an allow_only attribute at the class level. All the methods in this\n        controller will require the same level of access. You need to be manager to\n        access <a href="')
            __M_writer(escape(tg.url('/secc')))
            __M_writer(u'">secc</a> or <a href=\n        "')
            __M_writer(escape(tg.url('/secc/some_where')))
            __M_writer(u'">secc/some_where</a>.</p>\n      </div>\n    </div>\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\nLearning TurboGears 2.3: Quick guide to the Quickstart pages.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 5, "35": 25, "36": 26, "37": 29, "38": 49, "39": 49, "40": 95, "41": 96, "42": 118, "43": 118, "44": 127, "45": 127, "46": 132, "47": 132, "48": 136, "49": 136, "50": 137, "51": 137, "52": 141, "58": 3, "62": 3, "68": 62}, "uri": "/home/masoud/Desktop/parsidan/parsidan/templates/about.mak", "filename": "/home/masoud/Desktop/parsidan/parsidan/templates/about.mak"}
__M_END_METADATA
"""
