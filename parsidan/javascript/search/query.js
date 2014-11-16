/**
 * Created by vahid on 10/9/14.
 */

parsidan.search.QueryStatus = {
  success: 0,
  not_found: 1,
  persian_word: 2
};

Class('parsidan.search.Query', parsidan.ParentalElement, {
  defaultOptions: {

  },
  __init__: function (word, options) {
    this.word = word;
    this.callSuper(parsidan.ParentalElement, '__init__', [word, options]);
    this.state = null;
    this.result = null;
    this.error = null;
    this.bindEvents();
    this.request();
  },
  bindEvents: function () {
    var self = this;
    this.$().find('button.close').click(function () {
      self.remove();
    });
  },
  remove: function () {
    var self = this,
      $queryInput = parsidan.searchEngine.$();
    self.callCallback(self.options.complete);
    self.$().remove();

    if ($queryInput.val().sanitize().hashCode() == self.word.hashCode()) {
      $queryInput.val('');
    }
  },
  request: function () {
    var self = this;
    this.transition(parsidan.search.LoadingState);
    this.xhr = $.ajax({
      url: parsidan.searchEngine.options.query.action,
      data: {
        word: this.word
      },
      success: function (resp, status, xhr) {
        var queryStatus = parsidan.search.QueryStatus;

        if (status == 'success' && resp.hasOwnProperty('status')) {
          self.queryStatus = resp.status;
          switch (resp.status) {
            case queryStatus.success:
              self.result = resp.result;
              self.transition(parsidan.search.SuccessState);
              break;
            case queryStatus.not_found:
              self.transition(parsidan.search.NoResultState);
              break;
            case queryStatus.persian_word:
              self.transition(parsidan.search.PersianWordState);
              break;
          }
        }
        else {
          self.error = parsidan.messages.query.fatal.format(self.word);
          self.transition(parsidan.search.FatalState);
        }
      },
      error: function (xhr, status, error) {
        self.error = error;
        self.transition(parsidan.search.FatalState);
      },
      complete: function (xhr, textStatus) {
        self.callCallback(self.options.complete);
      }
    });
  },
  transition: function (stateClass) {
    if (this.state) {
      this.state.dispose();
    }
    if (stateClass) {
      this.state = new stateClass(this);
    }
  },
  abort: function () {
    this.xhr.abort();
    this.transition(null);
    this.$().remove();
  },
  $content: function () {
    return this.$().find('.query-content');
  },
  $title: function () {
    return this.$().find('.query-title');
  },
  moveUp: function () {
    this.$().remove().prependTo(this.parent());
    this.bindEvents();
  }


}).StaticMembers({
  templateSelector: '#queryTemplate',
  $getParent: function(){
    return parsidan.searchEngine.$resultArea();
  }
});