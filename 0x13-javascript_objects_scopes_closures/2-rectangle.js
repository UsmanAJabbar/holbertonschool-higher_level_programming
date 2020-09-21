#!/usr/bin/node
// Generates a rectangle class with height and width
module.exports = class Rectangle {
  constructor (width, height) {
    if (width > 1 && height > 1) {
      this.width = width;
      this.height = height;
    }
  }
};
