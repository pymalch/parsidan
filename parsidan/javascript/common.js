
Class('parsidan.ConfigurableElement', {
  defaultOptions: {},
  __init__: function (options) {
    this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);
  }
});


Class('parsidan.CallbackCaller', parsidan.ConfigurableElement, {
  __init__: function (options) {
    this.callSuper(parsidan.ConfigurableElement, '__init__', [options]);
  },
  callCallback: function (callback, args) {
    if (callback) {
      if (typeof callback == 'string') {
        callback = this.options[callback];
      }
      callback.apply(this, args);
    }
  }
});

Class('parsidan.dictionary.Engine', parsidan.CallbackCaller, {

  defaultOptions: {
    query: {
      action: '/query.json'
    },
    complete: function () {
      self.currentProcedure = null;
    },
    resultAreaSelector: '.result-area',
    queryButtonSelector: '.btn-send',
    guest: true
  },


  __init__: function (inputObject, options) {
    this.input = inputObject;
    this.currentProcedure = null;
    this.expression = '';
    this.options = $.extend({}, this.__class__.prototype.defaultOptions, options);
    this.setUp();
  },

  setUp: function () {
    var self = this;
    this.input.keypress(function (e) {
      self.keyPressed(e);
    });
    $(this.options.queryButtonSelector).click(function (e) {
      e.charCode = 13;
      self.keyPressed(e);
      e.preventDefault();
      return false;
    });
  },

  $resultArea: function () {
    return $(this.options.resultAreaSelector);
  },

  proccess: function () {
    throw "Not Implemented!";
  },

  keyPressed: function (e) {
    var newExpression = this.input.val().sanitize();
    if (newExpression != this.expression) {
      this.expression = newExpression;
      if (e.charCode == 13) {
        this.proccess();
        this.input.select();
      }
    }
  }

});

parsidan.dictionary.responseStatus = {
  0: 'NoResultState',
  1: 'ForeignWordState',
  2: 'PersianWordState',
  4: 'ContributionAddedBeforeState',
  3: 'ContributionSuccessAddState',
  5: 'ContributionNotForeignState',
  6: 'ContributionNotPersianState'
};

/**
 * Abstract class for dictionary model
 * @abstract
 */
Class('parsidan.dictionary.Model', parsidan.CallbackCaller, {
  defaultOptions: {
    publicStates: {
      loading: 'LoadingState',
      fatal: 'FatalState'
    }
  },

  /**
   *
   * @param word
   * @param options
   * @private
   */
  __init__: function (word, options) {
    this.word = word;
    this.callSuper(parsidan.CallbackCaller, '__init__', [options]);
    this.state = null;
    this.result = null;
    this.sourceLang = null;
    this.error = null;
    this.bindEvents();
    this.request();
  },

  bindEvents: function () {
  },

  remove: function () {

  },

  /**
   *
   * @returns {{word: *}}
   */
  requestData: function () {
    return {
      word: this.word
    }
  },

  request: function () {
    var self = this;
    this.transition(self.options.publicStates.loading);
    this.xhr = $.ajax({
      url: self.options.query.action,
      data: self.requestData(),
      success: function (resp, status, xhr) {
        if (status == 'success' && resp.hasOwnProperty('status')) {
          self.result = resp.result;
          self.transition(parsidan.dictionary.responseStatus[resp.status]);
        }
        else {
          self.error = parsidan.messages.query.fatal.format(self.word);
          self.transition(self.options.publicStates.fatal);
        }
      },
      error: function (xhr, status, error) {
        self.error = error;
        self.transition(self.options.publicStates.fatal);
      },
      complete: function (xhr, textStatus) {
        self.callCallback(self.options.complete);
      }
    });
  },

  transition: function (stateClass) {
    if (this.state) {
      this.state.dispose();
    }
    if (stateClass) {
      var fn = window.parsidan.dictionary.stateClass;
      this.state = new fn(this);
    }
  },

  abort: function () {
    this.xhr.abort();
    this.transition(null);
    this.$().remove();
  },


  moveUp: function () {
    this.$().remove().prependTo(this.parent());
    this.bindEvents();
  },

  $: function () {
    throw "Not Implemented!";
  },

  $equivalentsArea: function () {
    return this.$().find('.%s'.format(this.__class__.equivalentsAreaClass));
  },


  $equivalentsWords: function () {
    return this.$().find('.%s'.format(this.__class__.equivalentsWordsClass));
  },

  $equivalentsForm: function () {
    return this.$().find('.%s'.format(this.__class__.equivalentsFormClass));
  },

  $equivalentsInput: function () {
    return this.$().find('.%s'.format(this.__class__.equivalentsInputClass));
  },

  $equivalentsItems: function () {
    var items = this.$().find('.%s'.format(this.__class__.equivalentsItemsClass));
    if (items.length){
      return items;
    }
    else {
      return $('<ul />').addClass(this.__class__.equivalentsItemsClass)
        .appendTo(this.$equivalentsWords());
    }
  },


  $question: function () {
    var question = this.$().find(this.__class__.questionTemplate.cssClass);
    if (question.length){
      return question;
    }
    else{
      return $(this.__class__.questionTemplate.id)
        .clone()
        .removeAttr('id')
        .removeClass('hidden');
    }
  }

}).StaticMembers({

  templateSelector: '#queryTemplate',
  questionTemplate: {
    id: '#questionTemplate',
    cssClass: '.question'
  },
  equivalentsFormClass: 'equivalents-form',
  equivalentsInputClass: 'input-equivalent',
  equivalentsAreaClass: 'equivalents-area',
  equivalentsWordsClass: 'words',
  equivalentsItemsClass: 'equivalents-items',
  $getParent: function () {
    return parsidan.dictionary.Engine.$resultArea();
  }

}); // parsidan.dictionary.Model


