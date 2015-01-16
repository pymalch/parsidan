/**
 * Created by vahid on 10/9/14.
 */



Class('parsidan.dictionary.States', {
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

Class('parsidan.dictionary.LoadingState', parsidan.dictionary.States, {
  elements:{
      loadingSelector:'loading',
      loadingImage:'/img/preloader.gif'
  },
  $loading:function(){
      var loading=this.query.$content().find('.%s'.format(this.__class__.prototype.elements.loadingSelector))
      if(loading.length)
        return loading;
      else
        return $('<img />').addClass(this.__class__.prototype.elements.loadingSelector).attr({
      src: this.__class__.prototype.elements.loadingImage
    });

  },
  setUp: function(){
     this.query.$().addClass('panel-primary');
    this.query.$title().text(parsidan.messages.dictionary.loading.format(this.query.word));
    this.$loading().appendTo(this.query.$content());

  },
  dispose: function(){
    this.query.$title().empty();
    this.$loading().remove();
    this.query.$().removeClass('panel-primary');
  }
});





Class('parsidan.dictionary.ForeignWordState', parsidan.dictionary.States, {
  setUp: function(){
    this.query.$().addClass('panel-default persian');
    this.query.$title().html(parsidan.messages.dictionary.foreignEquivalents.format(this.query.word));
    this.query.sourceLang='foreign';
    this.query.equivalentLang='persian';
    this.query.bindEvents();

    for(var i in this.query.result){
    var item = this.query.result[i];
    $('<li />').html(item.title).appendTo(this.query.$equivalentsItems());
    }
  },
  dispose: function(){

  }
});

Class('parsidan.dictionary.PersianWordState', parsidan.dictionary.States, {
  setUp: function(){
    var self = this;
    this.query.$title().html(parsidan.messages.dictionary.persianEquivalents.format(this.query.word));
    this.query.sourceLang='persian';
    this.query.equivalentLang='foreign';
    this.query.bindEvents();
     for(var i in this.query.result){
      var item = this.query.result[i];

      $('<li />')
        .html(item.title)
          .append(function(){
          if(!self.query.options.guest)
            return '<i class="glyphicon glyphicon-thumbs-up"></i> <i class="glyphicon glyphicon-thumbs-down"></i>';
      })
        .appendTo(this.query.$equivalentsItems());
    }
  },
  dispose: function(){

  }
});


Class('parsidan.dictionary.NoResultState', parsidan.dictionary.States, {
  setUp: function(){
    this.query.$().addClass('panel-warning');
    this.query.$title().text(parsidan.messages.dictionary.noResult.format(this.query.word));
      if(!this.query.options.guest){
        this.query.$question()
            .prepend(parsidan.messages.dictionary.isWordPersian.format(this.query.word))
            .appendTo(this.query.$content());
        this.query.bindEvents();
    }

  },
  dispose: function(){
    this.query.$title().empty();
    this.query.$().removeClass('panel-warning');
    this.query.$question().remove();
  }
});






Class('parsidan.dictionary.FatalState', parsidan.dictionary.States, {
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




Class('parsidan.dictionary.ContributionLoadingState', parsidan.dictionary.States, {
  elements:{
      loadingSelector:'loading',
      loadingImage:'/img/preloader.gif'
  },
  $loading:function(){
      var loading=this.query.$equivalentsWords().find('.%s'.format(this.__class__.prototype.elements.loadingSelector))
      if(loading.length)
        return loading;
      else
        return $('<img />').addClass(this.__class__.prototype.elements.loadingSelector).attr({
      src: this.__class__.prototype.elements.loadingImage
    });

  },
  setUp: function(){
   this.query.$equivalentsWords().find('.alert').remove();
   this.$loading().prependTo(this.query.$equivalentsWords());
  },
  dispose: function(){
    this.$loading().remove();
  }
});


Class('parsidan.dictionary.ContributionSuccessAddState', parsidan.dictionary.States, {
  setUp: function(){
    $('<div/>').addClass('alert alert-success')
        .prependTo(this.query.$equivalentsWords())
        .html(parsidan.messages.dictionary.persianAddedSuccess . format(this.query.word));
       $('<li/>').text(this.query.word)
          .appendTo(this.query.$equivalentsItems());
  },
  dispose: function(){
    alert('dispose of state ');
    this.query.$equivalentsWords().find('.alert').remove();
  }
});

Class('parsidan.dictionary.ContributionNotForeignState', parsidan.dictionary.States, {
  setUp: function(){
alert('ContributionNotForeignState');
  },
  dispose: function(){

  }
});

Class('parsidan.dictionary.ContributionNotPersianState', parsidan.dictionary.States, {
  setUp: function(){
    $('<div/>').addClass('alert alert-warning')
        .prependTo(this.query.$equivalentsWords())
        .html(parsidan.messages.dictionary.foreignWordError . format(this.query.word));

  },
  dispose: function(){
     this.query.$equivalentsWords().find('.alert').remove();
  }
});
Class('parsidan.dictionary.ContributionAddedBeforeState', parsidan.dictionary.States, {
  setUp: function(){
    $('<div/>').addClass('alert alert-warning')
        .prependTo(this.query.$equivalentsWords())
        .html(parsidan.messages.dictionary.addedBefore . format(this.query.word));

  },
  dispose: function(){
     this.query.$equivalentsWords().find('.alert').remove();

  }
});


Class('parsidan.dictionary.ContributionFatalState', parsidan.dictionary.States, {
  setUp: function(){

  },
  dispose: function(){

  }
});



