/**
 * Created by Masoud on 10/9/14.
 */

Class('parsidan.manageWords.manage', parsidan.dictionary.Model, {


  __init__: function (controller,element) {
      console.log(controller);
      console.log(element);
      this.controller=controller;
      this.element=element


    var self = this;
    this.transition(self.options.publicStates.loading);
    this.xhr = $.ajax({
      url: controller.action,
      data: self.requestData(),
      success: function (resp, status, xhr) {

      },
      error: function (xhr, status, error) {

      },
      complete: function (xhr, textStatus) {

      }
    });
  },
 requestData: function(){
    return{
        id : this.__class__.getItemId(this.element)
    }

  },
  $:function(){
    return $(this.__class__.getElementId(this.__class__.getItemId(this.element)));
  }

}).StaticMembers({
    getItemId:function(element){
        return element.attr('data-rel');
    },
    getElementId: function(id){

        return '#w_%s'.format(id);
    }
});