<%def name="contribution_word_template(word=None)">
    <div class="panel panel-default contribution-word-template">
        <div class="panel-heading">
            <h3 class="panel-title">

                % if word:
                ${word.title}
                % endif

            </h3>
            </div>
            <div class="panel-body equivalent-content">

                <div class="form-group">
                <div class="input-group">

                    <input
                           type="text"
                           class="form-control"
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

</%def>