function xor(a, b) {
  return ( a || b ) && !( a && b );
}

String.prototype.hashCode = function () {
  var hash = 0;
  if (this.length == 0) return hash;
  for (var i = 0; i < this.length; i++) {
    hash = ((hash << 5) - hash) + this.charCodeAt(i);
    hash = hash & hash; // Convert to 32bit integer
  }
  return hash;
};

var sanitize_mappings = {
  '\u0643': '\u06A9',
  '\u06AB': '\u06A9',
  '\u06AA': '\u06A9',

  '\u064A': '\u06CC',
  '\u0649': '\u06CC',
  '\u06CD': '\u06CC',
  '\u06CE': '\u06CC',
  '\u06D3': '\u06CC',
  '\u06D2': '\u06CC',
  '\u06D1': '\u06CC',
  '\u06D0': '\u06CC'
};

String.prototype.sanitize = function () {
  var result = '',
    word = this.trim(),
    c = '';

  for (var i = 0; i < word.length; i++) {
    c = word.charAt(i);
    if (c in sanitize_mappings) {
      result += sanitize_mappings[c];
    }
    else {
      result += c;
    }
  }
  return result;
};

function escapeRegExp(string) {
    return string.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1");
}

String.prototype.replaceAll = function (find, replace) {
  return this.replace(new RegExp(escapeRegExp(find), 'g'), replace);
};