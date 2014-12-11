<%inherit file="local:templates.master"/>

<%
    col_classes = "col-md-8 col-md-offset-2"
%>


<div class="container contribution-words-area">
    <h1>${_('Persian words')}
        %if self_words:
                <small>
                ${_('Show my words')}
            </small>
        %endif
    </h1>
    <div class="contribution-notify-area alert"></div>

    <div class="filter">
        % if request.identity:
            %if self_words:
                <a href="${tg.url('/words')}" class="btn btn-primary">
                <i class="glyphicon glyphicon-filter"></i>
                ${_('Show all words')}
            </a>
            %else:
                ##todo: verify this url
                <a href="${tg.url('/words?self_words=1')}" class="btn btn-primary">
                <i class="glyphicon glyphicon-filter"></i>
                ${_('Show my words')}
            </a>
            %endif

        %endif
    </div>
    <div class="clearfix"></div>

    <div class="alphabets">
        %for i in alphabets:
            <a href="${tg.url('/words/%s' % i)}"  class="btn  ${('btn-default','btn-primary')[character==i]}">
                ${i}
            </a>
        %endfor
    </div>
    <div class="clearfix"></div>

    <div class="row">
        <div class="words-area">

        % for word in words:
           <div class="col-md-3 col-sm-6">
               <div class="panel panel-default">
                   <div class="panel-heading"><h3>${word.title}</h3></div>
               </div>
           </div>
        % endfor
        <div class="clearfix"></div>

        <ul class="pagination pagination-centered">
            ${tmpl_context.paginators.words.pager(page_link_template='<li><a%s>%s</a></li>',
              page_plain_template='<li class="active"><span%s>%s</span></li>')}
        </ul>


        </div>

    </div>
</div>

