/**
 * Created by vahid on 10/9/14.
 */

parsidan.search.ContributionStatus = {
  success: 0,
  added_before: 1,
  foreign_word: 2
};


Class('parsidan.contribution.SubmittedWord', parsidan.ParentalElement, {
  __init__: function (word, options) {
    this.word = word;
    this.callSuper(parsidan.ParentalElement, '__init__', [word, options]);
    this.error = null;
    this.request();
    this.result = null;
  },

  request: function () {
    var self = this;
    this.transition(parsidan.contribution.LoadingState);
    this.xhr = $.ajax({
      url: parsidan.contributionEngine.options.submit.action,
      data: {
        word: this.word
      },
      success: function (resp, status, xhr) {
        var contributionStatus = parsidan.search.ContributionStatus;
        if (status == 'success' && resp.hasOwnProperty('status')) {
          self.contributionStatus = resp.status;

          switch (resp.status) {
            case contributionStatus.success:
              self.transition(parsidan.contribution.SuccessState);
              break;
            case contributionStatus.added_before:
              self.result = resp.result;
              self.transition(parsidan.contribution.AddedBeforeState);
              break;
            case contributionStatus.foreign_word:
              self.transition(parsidan.contribution.ForeignWordState);
              break;
          }
        }
        else {
          self.error = parsidan.messages.submit.fatal.format(self.word);
          self.transition(parsidan.contribution.FatalState);
        }
      },
      error: function (xhr, status, error) {
        self.error = error;
        self.transition(parsidan.contribution.FatalState);
      },
      complete: function (xhr, textStatus) {
        self.callCallback('complete', [parsidan.contributionEngine.state]);
      }
    });
  },
  transition: function (stateClass) {
    if (parsidan.contributionEngine.state) {
      parsidan.contributionEngine.state.dispose();
    }
    if (stateClass) {
      parsidan.contributionEngine.state = new stateClass(this);
    }
  },
  abort: function () {
    this.xhr.abort();
    this.transition(null);
  },
  moveUp: function(){
    var parent = this.$().parent();
    this.$().remove().prependTo(parent);
    this.bindEvents();
  },
  $content: function () {
    return this.$().find('.panel-body');
  },
  $title: function () {
    return this.$().find('.panel-title');
  },

//  $templateTitle: null,
//  createTemplate: function () {
//    var self = this;
//
//    self.wordTemplate = parsidan.contributionEngine.$wordTemplate()
//      .clone()
//      .attr({
//        id: this.__class__.getElementId(this.word)})
//      .prependTo(parsidan.contributionEngine.$wordsArea());
//    self.wordTemplate.find('.panel-title').text(this.word);
//
//    if (self.result) {
//
//      var $ul = $('<ul />').appendTo(self.wordTemplate.find('.panel-body'));
//      for (var i in self.result) {
//        var item = self.result[i];
//        $('<li />')
//          .html(item.title)
//          .appendTo($ul);
//      }
//    }
//  },
  addForeignWord: function (translation) {

  }

}).StaticMembers({
  templateSelector: '#submittedWordTemplate',
  $getParent: function(){
    console.log(parsidan.contributionEngine.$wordsArea());
    return parsidan.contributionEngine.$wordsArea();
  }
});