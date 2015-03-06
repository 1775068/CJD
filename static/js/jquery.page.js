/*
* @author {y.g.q}
* @classDescription 分页
*/
(function ($) {

    $.pager = function (options) {
        var settings = {
            container: null,
            type: 'ajax',                   // ajax or url;
            pageCount: 0,                // 总条数;
            pageSize: 20,                // 页大小;
            callback: null                 // type = 'ajax'时调用此Function;
        };

        if (options) {
            $.extend(settings, options);
        }

        return new $.pager.fn.init(settings);
    };

    $.pager.fn = $.pager.prototype = {
        init: function (settings) {
            $.extend(this, settings);
            this.currPage = 1;                  // 当前页;
            this.totalPage = 0;                 // 总页数;

            return this;
        }
    };

    $.pager.fn.init.prototype = $.pager.fn;

    $.extend($.pager.fn, {

        // 输出html;
        toPage: function () {
            this.check();

            var obj = this.container, currPage = this.currPage, thas = this, pageSize = this.pageSize,

                pageCount = this.pageCount, prevPage = currPage - 1, nextPage = currPage + 1,

                totalPage = this.totalPage, e = 9, c = parseInt(e / 2), h = currPage - c, l = h + c * 2;
            
            obj.empty().append('<div class="info">显示 ' + (currPage * pageSize - pageSize+1) + ' 至 ' + (currPage * pageSize) + ' 条</div>');

            if (pageCount === 0) {
                return;
            }
            if (currPage <= c) {
                h = 0;
                l = l < pageCount ? e : pageCount;
            } else if (currPage + c >= pageCount) {
                h = pageCount - e + 1;
                l = pageCount;
            }

            var pageElem = $('<div class="page" />').appendTo(obj);

            var firstELem = $('<a class="first" href="javascript:;">首页</a>').appendTo(pageElem);
            // 上一页;
            if (prevPage < 1) {
                firstELem.addClass('n');
                pageElem.append('<a class="prev n" href="javascript:;">上一页</a>');
            } else {
                firstELem.click(function () { thas.to(1); });
                $('<a class="prev" href="javascript:;">上一页</a>').appendTo(pageElem).get(0).onclick = function () {
                    thas.to(prevPage);
                };
            }
            // 中间;
            var numElem = $('<em class="numbers">').appendTo(pageElem);
            for (var i = h; i <= l; i++) {

                if (i <= 0 || i > totalPage) {
                    continue;
                } else if (i === currPage) {
                    $('<a class="hover" href="javascript:;">' + i + '</a>').appendTo(numElem);
                } else {
                    $('<a href="javascript:;">' + i + '</a>').appendTo(numElem).get(0).onclick = (function (i) {
                        return function () {
                            thas.to(i);
                        }
                    })(i);
                }
            }

            var lastElem = $('<a class="last" href="javascript:;">末页</a>');
            if (nextPage > totalPage) {
                pageElem.append('<a class="next n" href="javascript:;">下一页</a>');
                lastElem.appendTo(pageElem).addClass('n');
            } else {
                $('<a class="next" href="javascript:;">下一页</a>').appendTo(pageElem).get(0).onclick = function () {
                    thas.to(nextPage);
                };
                lastElem.appendTo(pageElem).click(function () { thas.to(totalPage); });;
            }
        },

        check: function () {

            this.currPage = parseInt(this.currPage);
            this.totalPage = parseInt((this.pageCount - 1) / this.pageSize) + 1;

            if (this.currPage < 1) {
                this.currPage = 1;
            }
            if (this.totalPage < 1) {
                this.totalPage = 1;
            }
            if (this.currPage > this.totalPage) {
                this.currPage = this.totalPage;
            }

        },

        // 转至;
        to: function (page) {

            if (!isNaN(parseInt(page))) {

                this.currPage = page;
                if (this.type == "ajax") {
                    this.callback && this.callback.call(this, this.currPage);
                    this.toPage();
                } else {
                    self.location.href = YY.urlParam(self.location.href, "page", page);
                }
            } else {
                alert("出错啦!", "\u60a8\u4f20\u8f93\u7684\u9875\u7801\u6709\u8bef");
            }
        }
    });

    /**
     * @param {Element} listElem
     * @param {Element} pageElem
     * @param {Number} pageSize
     * @param {String} action
     * @param {String} url
     * @param {Object} urlData
     * @param {Function} callback
     */
    $.ajaxPager = function (options) {
        jQuery.pager({
            container: options.pageElem,
            type: 'ajax',
            pageSize: options.pageSize || 20,
            callback: function (pageIndex) {
                options.listElem.addClass('loading');
                var thas = this;
                if (options.urlData) {
                    options.urlData.pageIndex = pageIndex;
                }
                $[ options.action || 'post' ](options.url, options.urlData || {}, function (data) {
                    
                    options.listElem.children('ol').remove();

                    options.listElem.removeClass('loading');
                    thas.pageCount = data.RecordCount || 0;
                    thas.check();

                    options.callback && options.callback.call(thas, data, options);
                    thas.totalPage > 1 ? thas.toPage() : options.pageElem.empty();
                });
            }
        }).to(1);
    };

})(jQuery);