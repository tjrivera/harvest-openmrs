var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; },
  __hasProp = {}.hasOwnProperty,
  __extends = function(child, parent) { for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; } function ctor() { this.constructor = child; } ctor.prototype = parent.prototype; child.prototype = new ctor(); child.__super__ = parent.prototype; return child; };

define(['../core', './row'], function(c, row) {
  var Body, _ref;
  Body = (function(_super) {
    __extends(Body, _super);

    function Body() {
      this.itemViewOptions = __bind(this.itemViewOptions, this);
      _ref = Body.__super__.constructor.apply(this, arguments);
      return _ref;
    }

    Body.prototype.tagName = 'tbody';

    Body.prototype.template = function() {};

    Body.prototype.itemView = row.Row;

    Body.prototype.emptyView = row.EmptyRow;

    Body.prototype.itemViewOptions = function(model, index) {
      return c._.defaults({
        collection: model.data
      }, this.options);
    };

    return Body;

  })(c.Marionette.CollectionView);
  return {
    Body: Body
  };
});

/*
//@ sourceMappingURL=body.js.map
*/