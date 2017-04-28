#!/usr/bin/node
function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let i = 0; i < this.height; i++) {
      console.log(('X').repeat(this.width));
    }
  };
  this.rotate = function () {
    [this.width, this.height] = [this.height, this.width];
  };
  this.double = function () {
    this.width *= 2;
    this.height *= 2;
  };
}

function Square (size) {
  Rectangle.call(this, size, size);
}

Square.prototype.charPrint = function (c) {
  if (c === undefined) {
    for (let i = 0; i < this.height; i++) {
      console.log(('X').repeat(this.width));
    }
  } else {
    for (let i = 0; i < this.height; i++) {
      console.log((c).repeat(this.width));
    }
  }
};

module.exports = {Square};
