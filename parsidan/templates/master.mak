<!DOCTYPE html>
    <%
        lang = h.lang()
        min = '' if h.debug() else '.min'
        direction = '.rtl' if lang == 'fa' else '.ltr'
    %>
<html>
<head>
    <meta charset="${response.charset}"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${self.title()}</title>
    <link rel="stylesheet" type="text/css" media="screen" href="/css/public${direction}${min}.css"/>
    ${self.head_content()}
</head>
<body>

<%include file="local:templates.navigator" />

<div class="container">
    ${self.content_wrapper()}
</div>
    ${self.footer()}
<script type="text/javascript" src="/js/public${min}.js"></script>
    ${self.scripts()}
</body>
</html>

<%def name="content_wrapper()">
    <%
        flash=tg.flash_obj.render('flash', use_js=False)
    %>
    % if flash:
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                ${flash | n}
            </div>
        </div>
    % endif
    ${self.body()}
</%def>

<%def name="head_content()"></%def>

<%def name="title()">${_('Parsidan')}</%def>

<%def name="scripts()"></%def>

<%def name="footer()">
    <footer class="footer hidden-xs hidden-sm">
        <a class="pull-right" href="http://www.turbogears.org"><img style="vertical-align:middle;"
                                                                    src="${tg.url('/img/under_the_hood_blue.png')}"
                                                                    alt="TurboGears 2"/></a>

        <p>Copyright &copy; ${getattr(tmpl_context, 'project_name', 'TurboGears2')} ${h.current_year()}</p>
    </footer>
</%def>



