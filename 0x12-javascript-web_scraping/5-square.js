#!/usr/bin/node

const Rectangle = require('./5-rectangle.js').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

module.exports = { Square, Rectangle };
