Class('parsidan.contribution.Engine', parsidan.ElementController, {

  defaultOptions: {
    submit:{
      action: '/contribution/submit_persian_word'
    },
    wordsAreaSelector: '.words-area',
    addButtonSelector: '#btnQuery'


  },

  __init__: function (selector, options) {

    this.selector = selector;
    this.currentWord = null;
    this.state = null;
    this.word = '';
    this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);
    this.setUp();
  },
  setUp: function () {
    var self = this;
    this.$().keypress(function(e){
      self.keyPressed(e);
    });
    $(this.options.addButtonSelector).click(function(e){
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
  submitWord: function () {
    var self = this;
    if (this.word.length < 2) {
      return;
    }
    var element = parsidan.contribution.SubmittedWord.findLocal(this.word);
    if (element){
      parsidan.contribution.SubmittedWord.moveUp(element);

      if(self.state)
        self.state.dispose();
      return;
    }

    this.currentWord = parsidan.contribution.SubmittedWord.create(
      parsidan.contributionEngine.$wordsArea(),
      this.word,
      {
        complete: function(state) {
          self.state = state;
          self.currentWord = null;
        }
    });
  },
  keyPressed: function (e) {
    var newExpression = this.$().val().sanitize();
    if (newExpression != this.word) {
      this.word = newExpression;
      if (e.charCode == 13){
        this.submitWord();
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



