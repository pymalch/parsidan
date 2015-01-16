<!DOCTYPE html>
    <%
        lang = h.lang()
        min = '' if h.debug() else '.min'
        direction = '.rtl' if lang == 'fa' else '.ltr'
    %>
<!--
   ___                     _      __
  / _ \ ___ _  ____  ___  (_) ___/ / ___ _  ___
 / ___// _ `/ / __/ (_-< / / / _  / / _ `/ / _ \
/_/    \_,_/ /_/   /___//_/  \_,_/  \_,_/ /_//_/
-->
<html>
<head>
    <meta charset="${response.charset}"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <title>${self.title()}</title>
    <link rel="stylesheet" type="text/css" media="screen" href="/css/public${direction}${min}.css"/>
    ${self.head_content()}
</head>
<body>

<%include file="local:templates.navigator" />

<div class="container-fluid container-main">
    ${self.content_wrapper()}
</div>

<footer class="footer main-footer">
    <div class="container">
        <div class="center-block text-center copyright">
            ${_('&copy; %s Parsidan') % h.current_year() | n}
        </div>
    </div>
</footer>

<script type="text/javascript" src="/js/public${min}.js"></script>
<%include file="local:templates.client_messages" />
${self.scripts()}
</body>
</html>

<%def name="content_wrapper()">
    <%
        flash=tg.flash_obj.render('alert', use_js=False)
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



