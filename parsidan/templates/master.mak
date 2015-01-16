<!DOCTYPE html><html><!--

                                                                                            dddddddd
PPPPPPPPPPPPPPPPP                                                         iiii              d::::::d
P::::::::::::::::P                                                       i::::i             d::::::d
P::::::PPPPPP:::::P                                                       iiii              d::::::d
PP:::::P     P:::::P                                                                        d:::::d
  P::::P     P:::::Paaaaaaaaaaaaa  rrrrr   rrrrrrrrr       ssssssssss   iiiiiii     ddddddddd:::::d   aaaaaaaaaaaaa  nnnn  nnnnnnnn
  P::::P     P:::::Pa::::::::::::a r::::rrr:::::::::r    ss::::::::::s  i:::::i   dd::::::::::::::d   a::::::::::::a n:::nn::::::::nn
  P::::PPPPPP:::::P aaaaaaaaa:::::ar:::::::::::::::::r ss:::::::::::::s  i::::i  d::::::::::::::::d   aaaaaaaaa:::::an::::::::::::::nn
  P:::::::::::::PP           a::::arr::::::rrrrr::::::rs::::::ssss:::::s i::::i d:::::::ddddd:::::d            a::::ann:::::::::::::::n
  P::::PPPPPPPPP      aaaaaaa:::::a r:::::r     r:::::r s:::::s  ssssss  i::::i d::::::d    d:::::d     aaaaaaa:::::a  n:::::nnnn:::::n
  P::::P            aa::::::::::::a r:::::r     rrrrrrr   s::::::s       i::::i d:::::d     d:::::d   aa::::::::::::a  n::::n    n::::n
  P::::P           a::::aaaa::::::a r:::::r                  s::::::s    i::::i d:::::d     d:::::d  a::::aaaa::::::a  n::::n    n::::n
  P::::P          a::::a    a:::::a r:::::r            ssssss   s:::::s  i::::i d:::::d     d:::::d a::::a    a:::::a  n::::n    n::::n
PP::::::PP        a::::a    a:::::a r:::::r            s:::::ssss::::::si::::::id::::::ddddd::::::dda::::a    a:::::a  n::::n    n::::n
P::::::::P        a:::::aaaa::::::a r:::::r            s::::::::::::::s i::::::i d:::::::::::::::::da:::::aaaa::::::a  n::::n    n::::n
P::::::::P         a::::::::::aa:::ar:::::r             s:::::::::::ss  i::::::i  d:::::::::ddd::::d a::::::::::aa:::a n::::n    n::::n
PPPPPPPPPP          aaaaaaaaaa  aaaarrrrrrr              sssssssssss    iiiiiiii   ddddddddd   ddddd  aaaaaaaaaa  aaaa nnnnnn    nnnnnn


--><head>
    <%
        lang = h.lang()
        min = '' if h.debug() else '.min'
        direction = '.rtl' if lang == 'fa' else '.ltr'
    %>
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



