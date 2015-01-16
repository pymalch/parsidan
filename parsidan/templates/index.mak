<%inherit file="local:templates.master"/>

<%
    col_classes = "col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3"
%>
<div class="container query-area">
    <img src="/img/parsidan.jpg" class="center-block"/>

    <div class="row">
        <div class="${col_classes}">
            <div class="form-group">
                <div class="input-group input-group-lg">

                    <input id="queryInput"
                           type="text"
                           class="form-control"
                           placeholder="${ _('Please enter the word') }"
                           value="${word}">
                    <span class="input-group-btn">
                        <button class="btn btn-default btn-send" type="button" id="btnQuery">
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
</div>

<div id="searchEngineTemplates" class="hidden">
    <div id="queryTemplate" class="panel panel-default">
        <div class="panel-heading">
            <button type="button" class="close"><span aria-hidden="true">&times;</span><span
                    class="sr-only">Close</span></button>
            <h3 class="panel-title query-title"></h3>
        </div>
        <div class="panel-body query-content">

            <div class="equivalents-area">
                <div class="form-group equivalents-form hidden">
                    <div class="input-group">
                        <input type="text"
                               class="input-equivalent form-control"
                               placeholder=""
                               value="">
                        <span class="input-group-btn">
                            <button class="btn btn-default btn-send" type="button" id="btnQuery">
                                <span class="glyphicon glyphicon-plus"></span>
                            </button>
                        </span>
                    </div>
                </div>
                <div class="words">

                </div>
            </div>


        </div>
    </div>
</div>

<div class="question hidden" id="questionTemplate">
                <span> </span>
                <a href="javascript:;" class="yes" data-source="persian" data-equivalent="foreign" >${_('Yes')}</a>
                <a href="javascript:;" class="no"  data-source="foreign"  data-equivalent="persian" >${_('No')}</a>
            </div>


<%def name="scripts()">

    <script type="text/javascript">
        $(document).ready(function () {
            $('#queryInput').searchEngine({
                % if request.identity:
                    guest: false ,
                % endif
            }).select();
        });
    </script>
</%def>