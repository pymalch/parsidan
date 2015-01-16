
Class('parsidan.manageWords.Engine', parsidan.CallbackCaller, {

  defaultOptions: {
    query:{
      action: '/query.json'
    },
    complete: function(){
        self.currentProcedure = null;
     } ,
    linkSelector: '.make-link',
    removeButton: '.remove',
    notificationArea: '.notification-area'
  },
  __init__: function (linkObject , options) {

    this.currentProcedure = null;
    this.id = '';
    this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);

    this.setUp();
  },
  setUp: function () {
    var self = this;
    this.input.click(function(e){
        this.proccess();
    });
  },
  proccess: function () {
      alert('asdf');

  }
});

jQuery.fn.manageWordsEngine = function (options) {
    parsidan.manageWordsEngine = new parsidan.manageWords.Engine(this, options);

  return this;
};