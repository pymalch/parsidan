/**
 * Created by vahid on 10/9/14.
 */

Class('parsidan.search.QueryState', {
  __init__: function(query){
    this.query = query;
    this.alertTemplate = $('#searchEngineTemplates .alert')
    this.panelTemplate = $('#searchEngineTemplates .panel')

    this.setUp();
  },
  setUp: function(){
    throw "Not Implemented";
  },
  dispose: function(){
    throw "Not Implemented";
  }

});

Class('parsidan.search.LoadingState', parsidan.search.QueryState, {
  setUp: function(){
    $('<div />').addClass('loading').appendTo(this.query.selector);
    this.query.$title().text(parsidan.messages.query.loading.format(this.query.word));

    $('<img />').attr({
      src: "/img/preloader.gif"
    }).css('display','none').appendTo(this.query.$().find('.loading'));
    this.query.$().find('.loading img').slideDown();
  },
  dispose: function(){
    this.query.$().find('.loading').slideUp();
  }
});


Class('parsidan.search.SuccessState', parsidan.search.QueryState, {
  setUp: function(){

    this.panelTemplate.clone().appendTo(this.query.selector);
    this.query.$().find('.panel').addClass('panel-success');
    this.query.$title().text(parsidan.messages.query.success.format(this.query.word));
    var $ul = $('<ul />').appendTo(this.query.$content());
    for(var i in this.query.result){
      var item = this.query.result[i];
      $('<li />')
        .html(item.offer)
        .appendTo($ul);
    }
  }
});


Class('parsidan.search.NoResultState', parsidan.search.QueryState, {


  setUp: function(){

    this.alertTemplate.clone().appendTo(this.query.selector);
    this.query.$().find('.alert').addClass('alert-info').append(parsidan.messages.query.noResult.format(this.query.word));
  }
});

Class('parsidan.search.FatalState', parsidan.search.QueryState, {
  setUp: function(){

     this.alertTemplate.clone().appendTo(this.query.selector);
     this.query.$().find('.alert').addClass('alert-danger').append(parsidan.messages.query.fatal.format(this.query.word));
  }
});


Class('parsidan.search.PersianWordState', parsidan.search.QueryState, {
  setUp: function(){
          this.alertTemplate.clone().appendTo(this.query.selector);
    this.query.$().find('.alert').addClass('alert-success').append(this.query.word);

  }
});
