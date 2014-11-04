<%inherit file="local:templates.master"/>
<%namespace name="fn" file="parsidan.templates.defenitions"/>

<%
    col_classes = "col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3"
%>



<div class="container contribute-area">
    <div class="row">
        <div class="${col_classes}">
            <div class="form-group">
                <div class="input-group">

                    <input id="persianInput"
                           type="text"
                           class="form-control"
                           placeholder="${ _('Insert persian word') }"
                           value="">
                    <span class="input-group-btn">
                        <button class="btn btn-default" type="button" id="btnQuery">
                            <span class="glyphicon glyphicon-plus"></span>
                        </button>
                    </span>
                </div>
            </div>

             <div class="contribution-notify-area alert"></div>

              <div id="contribution_word_template" class="hidden">
                  ${fn.contribution_word_template()}
              </div>

            <div class="words-area"></div>

        </div>
    </div>
</div>


<%def name="scripts()">

    <script type="text/javascript">
        $(document).ready(function () {
            $('#persianInput').contributionEngine();
        });
    </script>
</%def>