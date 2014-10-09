/**
 * Created by vahid on 10/9/14.
 */



Class('parsidan.search.Query', parsidan.ElementController, {
  __init__: function(word){
    this.word = word;
    this.id = this.__class__.getElementId(word);
    this.selector = '#%s'.format(this.id);
    console.log('querying');
    console.log(this.$());
  },
  abort: function(){
    console.log('aborting');
  }


}).StaticMembers({
  templateSelector: '#queryTemplate',
  getElementId: function(word){
    return 'query_%s'.format(word.hashCode());
  },
  create: function(word){
    $(this.templateSelector)
      .clone()
      .attr({
        id: this.getElementId(word)})
      .find('.query-title').text(parsidan.messages.querying.format(word))
      .prependTo(parsidan.searchEngine.$resultArea());
    return new this(word);
  }
});