(function(env) {

    var listener = new window.keypress.Listener();

    var Car = function() {
        var _this = this;
        this.$buttons = $('.direction .button');
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
    };
    Car.prototype = {
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

    var Cam = function() {
        var _this = this;
        this.$buttons = $('.action .button');
        this.$buttons.bind('mousedown', function(e) {
            var $btn = $(this);
            var action = $btn.attr('action');
            switch(action) {
                case "camup":
                    _this.up();
                    break;
                case "camdown":
                    _this.down();
                    break;
                case "camleft":
                    _this.left();
                    break;
                case "camright":
                    _this.right();
                case "camneutral":
                    _this.neutral();
            }
        });
    };
    Cam.prototype = {
        up: function() {
            this._doAction('up');
        },
        down: function() {
            this._doAction('down');
        },
        left: function() {
            this._doAction('left');
        },
        right: function() {
            this._doAction('right');
        },
        stop: function() {
            this._doAction('stop');
        },
        neutral: function() {
            this._doAction('neutral');
        },
        _doAction: function(action) {
            $.ajax({
                'type': 'POST',
                'url': '/cam/'+action,
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

    var Controller = function() {}

    Controller.prototype = {

        init: function() {
            this.car = new Car();
            this.cam = new Cam();
        },
    };

    env.Controller = Controller;

})(window);
