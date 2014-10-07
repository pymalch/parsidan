<%inherit file="local:templates.master"/>

<div id="mainParsidan">
    <img src="${tg.url('/img/parsidan.jpg')}">
</div>
<div id="dictWrapper" class="fs1">
    <div id="fromLangWrapper">
        <input id="queryInput" type="text" class="form-control main-persian-input"
               placeholder="${ _('Please enter non persian word') }">

        <div class="messages">

            <div class="loading"><img src="img/preloader.gif"></div>
            <div class="noResult item">${ _('Persian translate for this word did not find!') }</div>
            <div class="wordAdded s1 item"> ${ _('Word stores is database to translate later.') }</div>
            <div class="addedWordBefore s2 item">${ _('Word is already added and is waiting for translation.') }</div>
            <div class="aPersianWord s3 item">${ _('The word you entered is already a persian word!') }</div>
        </div>

    </div>


</div>
<div class="join">${ _("You can %(join)s and help us to improve this dictionary.") % {'join': "JOIN US" } } </div>

<%def name="scripts()">

<script type="text/javascript">


    // Vahid:  My very own scope
    (function () {

        var statuses = {
                    ready: 0,
                    scheduled: 1,
                    querying: 2
                },
                searchEngine = {
                    expression: '',
                    selector: null,
                    action: '/query',
                    status: statuses.ready,
                    xhr: null,
                    timerId: null,
                    scheduleTimeout: 700,
                    $: function () {
                        return $(this.selector);
                    },
                    query: function () {
                        var self = this;
                        $.ajax({
                            url: '/query',
                            data: {
                                word: this.expression
                            },
                            success: function(resp, status, xhr){
                                console.log(status);
                            },
                            error: function(xhr, status, err){
                                console.log(status);
                            }

                        });

                    },
                    result: function(){},
                    schedule: function () {
                        var self = this;
                        this.status = statuses.scheduled;
                        this.timerId = setTimeout(function () {
                            self.query();
                        }, this.scheduleTimeout);
                    },
                    keyPressed: function () {
                        var newExpression = this.$().val();
                        if (newExpression != this.expression) {
                            this.expression = newExpression;

                            switch (this.status) {
                                case statuses.ready:
                                    break;
                                case statuses.scheduled:
                                    if (this.timerId != null) {
                                        clearTimeout(this.timerId);
                                    }
                                    break;
                                case statuses.querying:
                                    if (this.xhr != null) {
                                        this.xhr.abort();
                                    }
                                    break;
                            }

                            this.schedule();

                        }
                    },
                    setUp: function (selector) {
                        var self = this;
                        this.selector = selector;
                        this.$().keyup(function () {
                            self.keyPressed();
                        }).change(function () {
                            self.keyPressed();
                        });
                    }
                };

        searchEngine.setUp('#queryInput');

    })();


</script>
</%def>