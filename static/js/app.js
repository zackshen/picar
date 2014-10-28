(function(env) {

    var Controller = function() {
        var _this = this;
        this.$buttons = $('.button');
        this.$buttons.bind('mousedown', function(e) {
            var $btn = $(this);
            var action = $btn.attr('action');
            switch(action) {
                case "forward":
                    _this.forward();
                    break;
                case "backward":
                    _this.backward();
                    break;
                case "left":
                    _this.left();
                    break;
                case "right":
                    _this.right();
                    break;
            }
        });
        this.$buttons.bind('mouseup', function(e) {
            var $btn = $(this);
            var action = $btn.attr('action');
            switch(action) {
                case "forward":
                    _this.stop();
                    break;
                case "backward":
                    _this.stop();
                    break;
                case "left":
                    _this.stop();
                    break;
                case "right":
                    _this.stop();
                    break;
            }
        });
    }

    Controller.prototype = {

        init: function() {
            this._doAction('blink');
        },
        forward: function() {
            this._doAction('forward');
        },
        backward: function() {
            this._doAction('backward');
        },
        left: function() {
            this._doAction('turnleft');
        },
        right: function() {
            this._doAction('turnright');
        },
        stop: function() {
            this._doAction('stop');
        },
        _doAction: function(action) {
            $.ajax({
                'type': 'POST',
                'url': '/car/'+action,
                'dataType': 'JSON',
                'success': function(result) {
                    console.log(result);
                },
                'error': function(error) {
                    console.log(error);
                }
            });
        }
    };

    env.Controller = Controller;

})(window);
