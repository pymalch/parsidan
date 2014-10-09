var Status = parsidan.search.Status = {
    ready: 0,
    scheduled: 1,
    querying: 2
};



Class('parsidan.search.Engine', parsidan.ElementController, {


    defaultOptions: {
        action: '/query.json',
        scheduleTimeout: 700,
        templatesSelector: '#templates'
    },

    __init__: function(selector, options){
        this.selector = selector;
        this.status = Status.ready;
        this.xhr= null;
        this.timerId= null;
        this.expression= '';
        this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);
        this.setUp();
    },
    $templates: function(){
      return $(this.options.templatesSelector);
    },
    setUp: function () {
        var self = this;
        this.$().keyup(function () {
            self.keyPressed();
        }).change(function () {
            self.keyPressed();
        });
    },

    query: function () {
        var self = this;
        $.ajax({
            url: this.options.action,
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
        new parsidan.search.Result(resp);
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
        }, this.options.scheduleTimeout);
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
    }
});

jQuery.fn.searchEngine = function(options){
  if (this.length >= 1 && !parsidan.hasOwnProperty('searchEngine')){
    parsidan.searchEngine = new parsidan.search.Engine(this.selector, options);
  }
  return this;
};



