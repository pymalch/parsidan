/**
 * Created by vahid on 10/9/14.
 */

Class('parsidan.search.QueryState', {
  __init__: function(query){
    this.query = query;

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

    this.query.$title().text(parsidan.messages.query.loading.format(this.query.word));

    $('<img />').attr({
      src: "/img/preloader.gif"
    }).appendTo(this.query.$content());

  },
  dispose: function(){
    this.query.$title().empty();
    this.query.$content().empty();
  }
});


Class('parsidan.search.SuccessState', parsidan.search.QueryState, {
  setUp: function(){
    this.query.$title().text(parsidan.messages.query.success.format(this.query.word));
    var $ul = $('<ul />').appendTo(this.query.$content());
    for(var i in this.query.result){
      var item = this.query.result[i];
      $('<li />')
        .html(item.offer)
        .appendTo($ul);
    }
  },
  dispose: function(){
    this.query.$title().empty();
  }
});


Class('parsidan.search.NoResultState', parsidan.search.QueryState, {
  setUp: function(){
    this.query.$title().text(parsidan.messages.query.noResult.format(this.query.word));
  },
  dispose: function(){
    this.query.$title().empty();
  }
});

