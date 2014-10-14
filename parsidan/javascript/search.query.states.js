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
    this.query.$().addClass('panel-primary');
    this.query.$title().text(parsidan.messages.query.loading.format(this.query.word));

    $('<img />').attr({
      src: "/img/preloader.gif"
    }).appendTo(this.query.$content());

  },
  dispose: function(){
    this.query.$title().empty();
    this.query.$content().empty();
    this.query.$().removeClass('panel-primary');
  }
});


Class('parsidan.search.SuccessState', parsidan.search.QueryState, {
  setUp: function(){
    this.query.$().addClass('panel-success');
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
    this.query.$content().empty();
    this.query.$().removeClass('panel-success');
  }
});


Class('parsidan.search.NoResultState', parsidan.search.QueryState, {
  setUp: function(){
    this.query.$().addClass('panel-warning');
    this.query.$title().text(parsidan.messages.query.noResult.format(this.query.word));
    this.query.$content().addClass('no-padding');
  },
  dispose: function(){
    this.query.$title().empty();
    this.query.$().removeClass('panel-warning');
    this.query.$content().removeClass('no-padding');
  }
});

Class('parsidan.search.FatalState', parsidan.search.QueryState, {
  setUp: function(){
    this.query.$().addClass('panel-danger');
    this.query.$title().text(parsidan.messages.query.fatal.format(this.query.word));
    $('<p />')
      .addClass('error')
      .html(this.query.error)
      .appendTo(this.query.$content());
  },
  dispose: function(){
    this.query.$title().empty();
    this.query.$content().empty();
    this.query.$().removeClass('panel-danger');
  }
});


Class('parsidan.search.PersianWordState', parsidan.search.QueryState, {
  setUp: function(){
    this.query.$().addClass('panel-info');
    this.query.$title().text(this.query.word);
    $('<p />')
      .html(parsidan.messages.query.persian_word.format(this.query.word))
      .appendTo(this.query.$content());
  },
  dispose: function(){
    this.query.$title().empty();
    this.query.$content().empty();
    this.query.$().removeClass('panel-info');
  }
});
