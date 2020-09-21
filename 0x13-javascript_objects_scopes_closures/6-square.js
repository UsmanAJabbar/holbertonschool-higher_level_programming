#!/usr/bin/node
// Generates a square class
const LastGenSquare = require('./5-square');
module.exports = class Square extends LastGenSquare {
  // Dynamically calls on the print function with
  // a preset character that prints a visualization
  // of the rectangle/square class
  charPrint (c) { this.print(c); }
};
