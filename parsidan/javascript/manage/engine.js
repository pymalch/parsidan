
Class('parsidan.manageWords.Engine', parsidan.CallbackCaller, {

  defaultOptions: {
    complete: function(){
        self.currentProcedure = null;
     } ,
    notificationArea: '.notification-area',
    defaultEvent: 'click'
  },
  controllers:{
      'setEquivalent':{
          action:'/manage/setEquivalents',
          listenerSelector: '.link'
      },
      'removeWord':{
          action:'/manage/removeWord',
          listenerSelector: '.remove'

      },
      rateEquivalents:{
           action:'/manage/rateWord',
          listenerSelector: '.rate'
      }
  },
  __init__: function ( options) {

    this.procedures = new Array();
    this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);
    this.controllers= this.__class__.prototype.controllers;

    this.setUp();
  },
  setUp: function() {
    var self = this;

    $.each(self.controllers,function(k,v){
        var controller=this;
        if(!this.event){
            this.event= self.options.defaultEvent;
        }

        $(this.listenerSelector).bind(this.event, function(){
           self.procedures[controller]=new parsidan.manageWords.manage(controller,this);
        });

    });

  }

}).StaticMembers({

});

jQuery.fn.manageWordsEngine = function (options) {
    parsidan.manageWordsEngine = new parsidan.manageWords.Engine( options);

  return this;
};