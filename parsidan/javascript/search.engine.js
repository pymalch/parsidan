//var Status = parsidan.search.Status = {
//  ready: 0,
//  scheduled: 1,
//  querying: 2
//};


Class('parsidan.search.Engine', parsidan.ElementController, {


  defaultOptions: {
    query:{
      action: '/query.json',
    },
    scheduleTimeout: 700,
    resultAreaSelector: '.result-area',

  },

  __init__: function (selector, options) {
    this.selector = selector;
    this.currentQuery = null;
    this.timerId = null;
    this.expression = '';
    this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);
    this.setUp();
  },
  setUp: function () {
    var self = this;
    this.$().keyup(function () {
      self.keyPressed();
    }).change(function () {
      self.keyPressed();
    });
  },
  $resultArea: function () {
    return $(this.options.resultAreaSelector);
  },
  query: function () {
    var self = this;
    if (this.expression.length < 2) {
      return;
    }
    this.currentQuery = parsidan.search.Query.create(this.expression, {
      complete: function(){
        self.currentQuery = null;
      }
    });
  },
  schedule: function () {
    var self = this;
    this.timerId = setTimeout(function () {
      this.timerId = null;
      self.query();
    }, this.options.scheduleTimeout);
  },
  keyPressed: function () {
    var newExpression = this.$().val();
    if (newExpression != this.expression) {
      this.expression = newExpression;

      if (this.timerId != null) {
        clearTimeout(this.timerId);
      }

      if (this.currentQuery != null) {
        this.currentQuery.abort();
      }

      this.schedule();

    }
  }
});

jQuery.fn.searchEngine = function (options) {
  if (this.length >= 1 && !parsidan.hasOwnProperty('searchEngine')) {
    parsidan.searchEngine = new parsidan.search.Engine(this.selector, options);
  }
  return this;
};



