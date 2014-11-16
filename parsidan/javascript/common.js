
Class('parsidan.ConfigurableElement', {
  defaultOptions: {},
  __init__: function(options){
    this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);
  }
});

Class('parsidan.CallbackCaller', parsidan.ConfigurableElement, {
  __init__: function(options){
    this.callSuper(parsidan.ConfigurableElement, '__init__', [options]);
  },
  callCallback: function (callback, args) {
    if (callback) {
      if (typeof callback == 'string'){
        callback = this.options[callback];
      }
      callback.apply(this, args);
    }
  }
});

Class('parsidan.ElementController', parsidan.CallbackCaller, {
  __init__: function(key, options){
    this.callSuper(parsidan.CallbackCaller, '__init__', [options]);
    this.id = this.__class__.getElementId(key);
    this.selector = '#%s'.format(this.id);
    this.$()[0].controller = this;
  },
  $: function () {
    if (!this.hasOwnProperty('selector')) {
      throw "Not Implemented: %s.selector property".format(this.__class__.__name__);
    }
    return $(this.selector);
  }

}).StaticMembers({
  getElementId: function (key) {
    return '%s_%s'.format(this.__name__.replaceAll('.', '_'), key.hashCode());
  }
});

Class('parsidan.TemplateDrivenElementController', parsidan.ElementController, {
  __init__: function(key, options){
    this.callSuper(parsidan.ElementController, '__init__', [key, options]);
  }
}).StaticMembers({
  getTemplate: function () {
    if (this.hasOwnProperty('templateSelector')) {
      return $(this['templateSelector']);
    }
    throw 'Not Implemented Error';
  },
  render: function (attributes) {
    var result = this.getTemplate().clone();
    if (attributes) {
      result.attr(attributes);
    }
    return result;
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
  }
});

Class('parsidan.ParentalElement', parsidan.TemplateDrivenElementController, {
  __init__: function(key, options){
    this.callSuper(parsidan.TemplateDrivenElementController, '__init__', [key, options]);
  },
  $parentElement: function(){
    return this.__class__.$getParent();
  }
}).StaticMembers({
  $getParent: function(){
    throw 'Not Implemented Error';
  },
  findLocal: function (key) {
    var $elements = this.$getParent().find('#%s'.format(this.getElementId(key)));
    if ($elements.length && $elements[0].controller) {
      return $elements[0].controller;
    }
    return null;
  }
});