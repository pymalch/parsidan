<%
    lang = h.lang()
%>
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
                <li>
                    <a href="/setlang/${('fa', 'en')[lang == 'fa']}">${(_('Persian'), _('English'))[lang == 'fa']}</a>
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