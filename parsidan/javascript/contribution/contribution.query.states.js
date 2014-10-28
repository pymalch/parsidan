/**
 * Created by vahid on 10/9/14.
 */

Class('parsidan.contribution.QueryState', {
  __init__: function(query){
    this.query = query;
    this.area= parsidan.contributionEngine.$notifyArea();

    this.setUp();
  },
  setUp: function(){
    throw "Not Implemented";
  },
  dispose: function(){
    throw "Not Implemented";
  }

});

Class('parsidan.contribution.LoadingState', parsidan.contribution.QueryState, {
  setUp: function(){
    this.area
        .append(
             $('<img />').attr({
                 src: "/img/preloader.gif"
              })
        );
  },
  dispose: function(){
   this.area.html('');
  }
});


Class('parsidan.contribution.SuccessState', parsidan.contribution.QueryState, {

  setUp: function(){
      this.area
          .html(parsidan.messages.contribution.success.format(this.query.word))
          .addClass('alert-success');
    this.query.createTemplate();

  },
  dispose: function(){
    this.area.removeClass('alert-success').html('');
    this.query.wordTemplate=null;
  }
});



Class('parsidan.contribution.FatalState', parsidan.contribution.QueryState, {
  setUp: function(){
    this.area
          .html(this.query.error)
          .addClass('alert-danger');
  },
  dispose: function(){
       this.area.removeClass('alert-danger').html('');

  }
});


Class('parsidan.contribution.AddedBeforeState', parsidan.contribution.QueryState, {
  setUp: function(){
        this.area
          .html(parsidan.messages.contribution.addedBefore.format(this.query.word))
          .addClass('alert-info');
  },
  dispose: function(){
        this.area.removeClass('alert-info').html('');
  }
});

Class('parsidan.contribution.ForeignWordState', parsidan.contribution.QueryState, {
  setUp: function(){
   this.area
          .html(parsidan.messages.contribution.foreignWord.format(this.query.word))
          .addClass('alert-warning');
  },
  dispose: function(){
      this.area.removeClass('alert-warning').html('');

  }
});
