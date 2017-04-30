#!/usr/bin/node
const Rectangle = require('./4-rectangle.js').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}

module.exports = { Square, Rectangle };
