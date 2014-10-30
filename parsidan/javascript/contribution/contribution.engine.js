
Class('parsidan.contribution.Engine', parsidan.ElementController, {

  defaultOptions: {
    query:{
      action: '/contribution/submit_persian_word'
    },
    wordsAreaSelector: '.words-area',
    queryButtonSelector: '#btnQuery',
    notifyAreaSelector: '.contribution-notify-area',
    templateSelector: '#contribution_word_template .contribution-word-template'

  },

  __init__: function (selector, options) {

    this.selector = selector;
    this.currentQuery = null;
    this.exState = null;
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
  $notifyArea: function () {
    return $(this.options.notifyAreaSelector);
  },
  $wordsArea: function () {
    return $(this.options.wordsAreaSelector);
  },
  $wordTemplate: function () {
    return $(this.options.templateSelector);
  },
  query: function () {
    var self = this;
    if (this.expression.length < 2) {
      return;
    }
    var element = parsidan.contribution.Query.findLocal(this.expression);
    if (element){
      parsidan.contribution.Query.moveUp(element);

      if(self.exState)
        self.exState.dispose();
      return;
    }

    this.currentQuery = new parsidan.contribution.Query(this.expression, {
      complete: function(state) {

        self.exState = state;
        self.currentQuery = null;
      }
    });
  },
  keyPressed: function (e) {
    var newExpression = this.$().val().sanitize();
    if (newExpression != this.expression) {
      this.expression = newExpression;
      if (e.charCode == 13){

        this.query();
        this.$().select();
      }
    }
  }
});

jQuery.fn.contributionEngine = function (options) {
  if (this.length >= 1 && !parsidan.hasOwnProperty('contributionEngine')) {
    parsidan.contributionEngine = new parsidan.contribution.Engine(this.selector, options);
  }
  return this;
};



