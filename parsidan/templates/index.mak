<%inherit file="local:templates.master"/>

<%
    col_classes = "col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3"
%>

<div class="container query-area">
    <img src="/img/parsidan.jpg" class="center-block"/>

    <div class="row">
        <div class="${col_classes}">
            <div class="form-group">
                <div class="input-group">

                    <input id="queryInput"
                           type="text"
                           class="form-control"
                           placeholder="${ _('Please enter non persian word') }"
                           value="${word}">
                    <span class="input-group-btn">
                        <button class="btn btn-default" type="button" id="btnQuery">
                            <span class="glyphicon glyphicon-search"></span>
                        </button>
                    </span>
                </div>
            </div>
        </div>
    </div>

</div>
<div class="container">
    <div class="row">
        <div class="${col_classes} result-area">

        </div>
    </div>
    ##    <div class="row messages">
    ##        <div class="col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3 text-align-auto">
    ##            <img class="center-block" src="img/preloader.gif" />
    ##            <div class="no-result">${ _('Persian translate for this word did not find!') }</div>
    ##            <div class="word-just-added"> ${ _('Word stores is database to translate later.') }</div>
    ##            <div class="word-already-added">${ _('Word is already added and is waiting for translation.') }</div>
    ##            <div class="word-is-persian">${ _('The word you entered is already a persian word!') }</div>
    ##            <div class="join-us">${ _("You can %(join)s and help us to improve this dictionary.") % {'join': "JOIN US" } } </div>
    ##        </div>
    ##    </div>
</div>
<div id="searchEngineTemplates" class="hidden">

    <div id="queryTemplate" class="panel panel-default">
        <div class="panel-heading">
            <button type="button" class="close"><span aria-hidden="true">&times;</span><span
                    class="sr-only">Close</span></button>
            <h3 class="panel-title query-title"></h3>
        </div>
        <div class="panel-body query-content">

        </div>
    </div>
</div>

<%def name="scripts()">

    <script type="text/javascript">
        $(document).ready(function () {
            $('#queryInput').searchEngine({
                scheduleTimeout: 1000
            });
        });
    </script>
</%def>