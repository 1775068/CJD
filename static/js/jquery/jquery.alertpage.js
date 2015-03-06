(function ($) {
    $.alertPage = function (options) {
        var settings = {
            'url': '',
            'data': {},
            'width': '300px',
            'height' : '400px'
        };
        if (options) {
            $.extend(settings, options);
        
        } 
        return new $.alertPage.prototype.init(settings);
    };
    $.alertPage.prototype.init = function (settings) {
        settings.url = YY.urlParam(settings.url, settings.data); 
        $('width,height'.split(',')).each(function () {
            settings[this] = parseInt(settings[this], 10);
        });
        settings.height && (settings.height+=30);
        $.extend(this, settings); 
        this.toHtml();
        this.wall();
    };
    $.alertPage.prototype.init.prototype = $.alertPage.prototype;
   
    $.extend($.alertPage.prototype, {
        'wall' : function(){
            this.wallElem = $('<div style="margin:0px;padding:0px;position:fixed;left:0px;top:0px;z-index:9999998;width:100%;height:100%;background-color:#000;display:none;" />').appendTo(document.body).css('opacity', .7);
        },
        'toHtml': function () {
            var thas = this, doc = document.documentElement, top = (doc.clientHeight - this.height) / 2 - 50, left = (doc.clientWidth - this.width) / 2,
                elem = this.elem = $('<div style="display:none;overflow:hidden;position:fixed;z-index:9999999;background: #F7F7F7;border: 1px solid #CDCDCD;border-radius: 3px;-webkit-border-radius: 3px;-moz-border-radius: 3px;box-shadow: 0 2px 2px -2px #CCC;margin-top: 25px;" />').appendTo(document.body)
                .css({ 'display': 'none', 'width': this.width, 'height': this.height, 'top': (top < 60 ? 60 : top) + 'px', 'left':left + 'px' });
            var hander = $('<div style="overflow:hidden;border-bottom: 1px solid #CDCDCD;box-shadow: 0 1px 0 white;-webkit-box-shadow: 0 1px 0 white;-moz-box-shadow: 0 1px 0 #fff;text-shadow: 0 1px white;-webkit-border-top-right-radius: 3px;-webkit-border-top-left-radius: 3px;-moz-border-radius-topright: 3px;-moz-border-radius-topleft: 3px;color: #636363;background: #F8F8F8;" />').appendTo(elem);
            this.title = $('<div style="float: left;display: block;padding: 8px 14px 7px 14px;font-size: 12px;font-weight: bold;text-shadow: 0 1px white;color: #636363;" />').appendTo(hander);
            var close = $('<div style="width:37px;height:30px;line-height:30px;float:right;position:relative;cursor:pointer;color: #636363;font-weight:bold;right:20px;">[关闭]</div>').appendTo(hander);
             var iframe = this.frame = $('<iframe frameborder="0" />').appendTo(elem).css({ 'width':this.width, 'height':this.height }).attr('src', this.url);
            
            // 遮挡select;
             $('<iframe frameborder="0" style="position:absolute;z-index:-1;top:0px;left:0px;" />').appendTo(elem).css({ 'width': this.width, 'height': this.height });
         
            close.click(function () { thas.hide(); });
        },
        'open': function (title, url, data, width, height) {
            title && this.title.text(title);
            data && (url = YY.urlParam(url, data));
            YY.is(url) === 'string' && this.frame.attr('src', url);
            width  && this.elem.css('width', width);
            height && this.elem.css('height', parseInt(height, 10) + 30);
            
            this.elem.css('display', 'block');
            this.wallElem.css('display', 'block');
        },
        'hide' : function(){
            this.elem.css('display', 'none');
            this.wallElem.css('display', 'none');
        },
        'remove': function () {
            this.elem.remove();
            this.wallElem.remove();
        }
    });
})(jQuery);