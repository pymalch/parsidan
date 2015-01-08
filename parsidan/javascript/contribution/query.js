/**
 * Created by vahid on 10/9/14.
 */

Class('parsidan.search.Query', parsidan.dictionary.Model, {

  __init__: function (word, options) {
    this.id = this.__class__.getElementId(word);
    this.selector = '#%s'.format(this.id);
    this.sourceLang , this.equivalentLang= null
    this.$()[0].controller = this;
    this.callSuper( parsidan.dictionary.Model, '__init__', [word, options]);
  },
  bindEvents: function () {
    var self = this;
    this.$().find('button.close').click(function () {
      self.$().remove();
    });

    self.$question().find('a').click(function () {
      self.sourceLang = $(this).attr('data-source');
        self.equivalentLang = $(this).attr('data-equivalent');
        self.$question().remove();
        self.$title().html('%s "%s"'.format(parsidan.messages.dictionary[
            '%sWord'.format(self.sourceLang)
            ],self.word));
        self.contribute();
     });
      if( self.sourceLang && self.equivalentLang)
        self.contribute();

  },

  remove: function () {
    var self = this,
      $queryInput = parsidan.searchEngine.$();
    self.callCallback(self.options.complete);
    self.$().remove();

    if ($queryInput.val().sanitize().hashCode() == self.word.hashCode()) {
      $queryInput.val('');
    }
  },
  moveUp: function () {
    this.$().remove().prependTo(parsidan.searchEngine.$resultArea());
    this.bindEvents();
  },
  contribute: function(){
      var self = this;
      self.$().removeClass().addClass('panel panel-default %s'.format(self.sourceLang));

      if(self.options.guest)
        return;



      self.$equivalentsForm().removeClass('hidden');
        self.$equivalentsInput().attr('placeholder' , parsidan.messages.dictionary['%sInputPlaceholder'.format(self.equivalentLang)]);
        self.$equivalentsInput().contributionEngine({
                wordPanel: self.$equivalentsArea(),
                query:{
                    action:'/contribution/submit-%s-word'. format( self.equivalentLang )
                },
                sourceWord: self.word
            });

  },
  $: function () {
    return $(this.selector);
  },
  $content: function () {
    return this.$().find(this.__class__.contentSelector);
  },
  $title: function () {
    return this.$().find(this.__class__.titleSelector);
  }

}).StaticMembers({
  templateSelector: '#queryTemplate',
  contentSelector: '.query-content',
  titleSelector: '.query-title',
  render: function (attributes) {
    var result = this.getTemplate().clone();
    if (attributes) {
      result.attr(attributes);
    }
    return result;
  },
  getTemplate: function () {
    if (this.hasOwnProperty('templateSelector')) {
      return $(this['templateSelector']);
    }
  },
  create: function (parent, key, options, attributes) {
    var attrs = {id: this.getElementId(key)};
    if (attributes){
      attrs = $.extend(attrs, attributes);
    }
    this
      .render(attrs)
      .prependTo(parent);
    return new this(key, options);
  },
  findLocal: function (key) {
    var $elements = this.$getParent().find('#%s'.format(this.getElementId(key)));
    if ($elements.length && $elements[0].controller) {
      return $elements[0].controller;
    }
    return null;
  },
  $getParent: function(){
    return parsidan.searchEngine.$resultArea();
  },
  getElementId: function (key) {
    return '%s_%s'.format(this.__name__.replaceAll('.', '_'), key.hashCode());
  }
});




Class('parsidan.contribution.Query', parsidan.dictionary.Model, {
    defaultOptions:{
        publicStates:{
            loading: 'ContributionLoadingState',
            fatal: 'ContributionFatalState'
        }
    },

  __init__: function (word, options) {

    this.callSuper( parsidan.dictionary.Model, '__init__', [word, options]);

  },
  bindEvents: function () {

  },

  remove: function () {

  },
 requestData: function(){

    return{
        word : this.word,
        sourceWord : this.options.sourceWord
    }

  },
  $: function(){
    return this.options.wordPanel;
  }

}).StaticMembers({

});