<%inherit file="local:templates.master"/>

<%
    col_classes = "col-xs-12 col-sm-10 col-sm-offset-1 col-md-6 col-md-offset-3"
%>



<div class="container contribute-area">
    <div class="row">
        <div class="${col_classes}">
            <div class="form-group">
                <div class="input-group input-group-lg">

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
            <div class="words-area"></div>

        </div>
    </div>
</div>


<div id="submittedWordTemplate" class="hidden">
    <div class="panel panel-default contribution-word-template">
        <div class="panel-heading">
            <h3 class="panel-title">
            </h3>
        </div>
        <div class="panel-body equivalent-content">
            <p class="message"></p>
            <div class="loading hidden"></div>
             <div class="form-group hidden" >
                <div class="input-group">
                    <input type="text"

                            class="input-foreign form-control"
                            placeholder="${ _('Please enter non persian word') }"
                            value="">
                    <span class="input-group-btn">
                        <button class="btn btn-default" type="button" id="btnQuery">
                            <span class="glyphicon glyphicon-plus"></span>
                        </button>
                    </span>
                </div>
            </div>
        </div>
    </div>
</div>


<%def name="scripts()">
    <script type="text/javascript">
        $(document).ready(function () {
            $('#persianInput').contributionEngine({
                onComplete:function(object){
                    this.state.word.$foreignInput().contributionEngine();
                }
            });

        });
    </script>
</%def>