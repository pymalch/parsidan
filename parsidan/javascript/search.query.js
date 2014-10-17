/**
 * Created by vahid on 10/9/14.
 */

parsidan.search.QueryStatus={
  success: 0,
  not_found: 1,
  persian_word: 2
};

Class('parsidan.search.Query', parsidan.ElementController, {
  __init__: function (word, callbacks) {
    this.word = word;
    this.id = this.__class__.getElementId(word);
    this.state = null;
    this.selector = '#%s'.format(this.id);
    this.result = null;
    this.error = null;
    this.callbacks = callbacks;
    this.$()[0].controller = this;
    this.bindEvents();
    this.request();
  },
  bindEvents: function(){
    var self = this;
    this.$().find('button.close').click(function(){
      self.remove();
    });
  },
  remove: function(){
    var self = this,
      $queryInput = parsidan.searchEngine.$();
    self.callbacks.complete.call(this);
    self.$().remove();

    if ($queryInput.val().sanitize().hashCode() == self.word.hashCode()){
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

        if (status == 'success' && resp.hasOwnProperty('status')){
          self.queryStatus = resp.status;
          switch(resp.status){
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
        else{
          self.error = parsidan.messages.query.fatal.format(self.word);
          self.transition(parsidan.search.FatalState);
        }
      },
      error: function (xhr, status, error) {
        self.error = error;
        self.transition(parsidan.search.FatalState);
      },
      complete: function (xhr, textStatus) {
        self.callbacks.complete.call(this);
      }
    });
  },
  transition: function (stateClass) {
    if (this.state) {
      this.state.dispose();
    }
    if (stateClass){
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
  moveUp: function(){
    var parent = this.$().parent();
    this.$().remove().prependTo(parent);
    this.bindEvents();
  }


}).StaticMembers({
    templateSelector: '#queryTemplate',
    getElementId: function (word) {
      return 'query_%s'.format(word.hashCode());
    },
    create: function (word, callbacks) {
      $(this.templateSelector)
        .clone()
        .attr({
          id: this.getElementId(word)})
        .prependTo(parsidan.searchEngine.$resultArea())
      return new this(word, callbacks);
    },
    findLocal: function(word){
      var panel = parsidan.searchEngine.$resultArea().find('#%s'.format(this.getElementId(word)));
      if (panel.length && panel[0].controller){
        return panel[0].controller;
      }
      return null;
    }
  });