<!DOCTYPE html>
    <%
        min = '.min' if h.debug() else ''
        direction = '.rtl' if h.lang() == 'fa' else '.ltr'
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
    ${self.main_menu()}
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

<%def name="main_menu()">
    <!-- Navbar -->
    <nav class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-content">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand navbar-logo" href="${tg.url('/')}">
                    <img src="/img/parsidan_logo.png" alt="${_('Parsidan')}}"/>
                </a>
            </div>

            <div class="collapse navbar-collapse" id="navbar-content">
                <ul class="nav navbar-nav">
                    <li class="${('', 'active')[page=='about']}">
                        <a href="/dictionary/alienList">${_('Make persian')}</a>
                    </li>
                    <li class="${('', 'active')[page=='about']}">
                        <a href="/dictionary/myWords">${_('My words')}</a>
                    </li>

                </ul>

                % if tg.auth_stack_enabled:
                    <ul class="nav navbar-nav navbar-right">
                        % if not request.identity:
                            <li><a href="${tg.url('/login')}">${_('Login')}</a></li>
                        % else:
                            <li><a href="${tg.url('/logout_handler')}">${_('Logout')}</a></li>
                            <li><a href="${tg.url('/admin')}">${_('Admin')}</a></li>
                        % endif
                    </ul>
                % endif
            </div>

        </div>


    </nav>
</%def>


