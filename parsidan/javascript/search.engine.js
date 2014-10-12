
Class('parsidan.search.Engine', parsidan.ElementController, {

  defaultOptions: {
    query:{
      action: '/query.json',
    },
    resultAreaSelector: '.result-area',
    queryButtonSelector: '#btnQuery'
  },

  __init__: function (selector, options) {
    this.selector = selector;
    this.currentQuery = null;
    this.expression = '';
    this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);
    this.setUp();
  },
  setUp: function () {
    var self = this;
    this.$().keypress(function(e){
      self.keyPressed(e);
    });
    $(this.options.queryButtonSelector).click(function(e){
      e.charCode = 13;
      self.keyPressed(e);
      e.preventDefault();
      return false;
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
    var localQuery = parsidan.search.Query.findLocal(this.expression);
    if (localQuery){
      localQuery.moveUp();
      return;
    }
    this.currentQuery = parsidan.search.Query.create(this.expression, {
      complete: function(){
        self.currentQuery = null;
      }
    });
  },

  keyPressed: function (e) {
    var newExpression = this.$().val();
    if (newExpression != this.expression) {
      this.expression = newExpression;
      if (e.charCode == 13){
        this.query();
      }
    }
  }
});

jQuery.fn.searchEngine = function (options) {
  if (this.length >= 1 && !parsidan.hasOwnProperty('searchEngine')) {
    parsidan.searchEngine = new parsidan.search.Engine(this.selector, options);
  }
  return this;
};



