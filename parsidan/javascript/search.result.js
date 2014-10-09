/**
 * Created by vahid on 10/9/14.
 */


Class('parsidan.search.Result', parsidan.ElementController, {
  __init__: function(data){
    this.word = data.word;
    this.id = 'result_%s'.format(this.word.hashCode());
    this.selector = '#%s'.format(this.id);
    this.data = data.result;
  },
  $content: function(){

  },
  render: function(){


  }
}).StaticMembers({
  template: ''
});
