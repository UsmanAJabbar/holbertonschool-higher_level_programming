#!/usr/bin/node
// Generates a square class
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  // Class attribute generator
  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    this.print(c)
  }
};
