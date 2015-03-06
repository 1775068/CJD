(function ($) {
    
    var yy = this.YY = this.YY || {},
        toString = Object.prototype.toString;

    yy.is = function (obj) {
        return toString.call(obj).toLowerCase().slice(8, -1);
    };
    yy.isarray = function (obj) {
        return yy.is(obj) === 'array';
    };
    yy.iselem = function (obj) {
        return yy.is(obj) === 'element';
    };
    yy.iselems = function (collection) {
        if (typeof collection !== 'object') return false;
        for (var d in collection) {
            return yy.is(collection[d]) === 'element';
        }
    };

    yy.mix = function (str, data) {
        return str.replace(/\$\{(\S+?)\}/gi, function (a, b) {

            return typeof data[b] === "undefined" ? a : data[b];
        });
    };


    //TODO:url;
    yy.queryString = function (key) {
        var value = location.search.match(new RegExp("[\?\&]" + key + "=([^\&]*)(\&?)", "i"));
        return value ? unescape(value[1]) : "";
    };
    yy.urlParam = function (url, key, value) {

        if (toString.call(key) === '[object Object]') {
            for (var i in key) {
                url = arguments.callee(url, i, key[i]);
            }
            return url;
        }
        key = encodeURIComponent(key);
        value = encodeURIComponent(value);
        if (url.indexOf('?') < 0) {
            return url + '?' + key + '=' + value;
        } else {
            var p = key + '=';
            if (url.indexOf('&' + p) < 0 && url.indexOf('?' + p) < 0) {
                return url + '&' + key + '=' + value;
            } else {
                var exp = new RegExp(key + '\=[^\\&]*', 'ig');
                return url.replace(exp, key + '=' + value);
            }
        }
    };

})(jQuery);