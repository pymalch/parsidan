Status = {
    ready: 0,
    scheduled: 1,
    querying: 2
};

Engine = {
    expression: '',
    selector: '#queryInput',
    action: '/query.json',
    status: Status.ready,
    xhr: null,
    timerId: null,
    scheduleTimeout: 700,
    $: function () {
        return $(this.selector);
    },
    query: function () {
        var self = this;
        $.ajax({
            url: this.action,
            data: {
                word: this.expression
            },
            success: function (resp, status, xhr) {
                self.result(resp);
            },
            error: function (xhr, status, err) {
                self.error(err);
            }

        });

    },
    result: function (resp) {
        console.log(resp);
    },
    noResult: function () {
        console.log('No result');
    },
    error: function (err) {
        console.log(err);
    },
    schedule: function () {
        var self = this;
        this.status = Status.scheduled;
        this.timerId = setTimeout(function () {
            self.query();
        }, this.scheduleTimeout);
    },
    keyPressed: function () {
        var newExpression = this.$().val();
        if (newExpression != this.expression) {
            this.expression = newExpression;

            switch (this.status) {
                case Status.scheduled:
                    if (this.timerId != null) {
                        clearTimeout(this.timerId);
                    }
                    break;
                case Status.querying:
                    if (this.xhr != null) {
                        this.xhr.abort();
                    }
                    break;
            }

            this.schedule();

        }
    },
    setUp: function () {
        var self = this;
        this.$().keyup(function () {
            self.keyPressed();
        }).change(function () {
            self.keyPressed();
        });
    }
};




parsidan.search = {
    EngineStatus: Status,
    Engine: Engine
};
