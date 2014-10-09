



Class('parsidan.CallbackCaller', {
  callCallback: function (callback, args) {
    if (callback) {
      callback.apply(this, args);
    }
  }
});

Class('parsidan.ElementController', parsidan.CallbackCaller, {
  $: function () {
    if (!this.hasOwnProperty('selector')){
      throw "Not Implemented: %s.selector property".format(this.__class__.__name__);
    }
    return $(this.selector);
  }

});