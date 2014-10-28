<%inherit file="local:templates.master"/>
<%namespace name="fn" file="parsidan.templates.defenitions"/>

<%
    col_classes = "col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3"
%>



<div class="container contribution-area">
    <div class="contribution-notify-area alert"></div>
    <div class="row">
        <div class="${col_classes} words-area">

        % for word in words:
            ${fn.contribution_word_template(word)}
        % endfor


        </div>
    </div>
</div>

