
Class('parsidan.search.Engine', parsidan.dictionary.Engine, {

   __init__: function(inputObject , options){
    this.callSuper(parsidan.dictionary.Engine, '__init__', [inputObject, options]);
  },
  preProccess:function(){
      var self = this;
    if (this.expression.length < 2) {
      return false;
    }
    var localItem = parsidan.search.Query.findLocal(this.expression);
    if (localItem){
      localItem.moveUp();
      return false;
    }
    return true;
  },
  proccess: function () {
    var self = this;
    if(!self.preProccess())
        return;
    this.currentProcedure = parsidan.search.Query.create(
      this.$resultArea(),
      this.expression, self.options);
  }
});

jQuery.fn.searchEngine = function (options) {
  if (this.length >= 1 && !parsidan.hasOwnProperty('searchEngine')) {
    parsidan.searchEngine = new parsidan.search.Engine(this, options);
  }
  return this;
};





Class('parsidan.contribution.Engine', parsidan.dictionary.Engine, {

   __init__: function(inputObject, options){
    this.callSuper(parsidan.dictionary.Engine, '__init__', [inputObject, options]);
  },
  proccess: function () {
    var self = this;
    this.currentProcedure = new parsidan.contribution.Query(this.expression, self.options);
  }
});


jQuery.fn.contributionEngine = function (options) {
    parsidan.contributionEngine = new parsidan.contribution.Engine(this, options);

  return this;
};



