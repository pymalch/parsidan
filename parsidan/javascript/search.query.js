/**
 * Created by vahid on 10/9/14.
 */



Class('parsidan.search.Query', parsidan.ElementController, {
  __init__: function (word) {
    this.word = word;
    this.id = this.__class__.getElementId(word);
    this.state = null;
    this.selector = '#%s'.format(this.id);
    this.result = null;
    this.request();
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
        console.log(resp);
        if (status == 'success'){
          self.result = resp.result;
          if (self.result.length <= 0){
            self.transition(parsidan.search.NoResultState);
          }
          else{
            self.transition(parsidan.search.SuccessState);
          }

        }
      },
      error: function () {

      },
      complete: function (xhr, textStatus) {

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
    console.log('aborting');
    this.xhr.abort();
    this.transition(null);
    this.$().remove();
  },
  $content: function () {
    return this.$().find('.query-content');
  },
  $title: function () {
    return this.$().find('.query-title');
  }


}).
  StaticMembers({
    templateSelector: '#queryTemplate',
    getElementId: function (word) {
      return 'query_%s'.format(word.hashCode());
    },
    create: function (word) {
      $(this.templateSelector)
        .clone()
        .attr({
          id: this.getElementId(word)})
        .prependTo(parsidan.searchEngine.$resultArea())
      return new this(word);
    }
  });