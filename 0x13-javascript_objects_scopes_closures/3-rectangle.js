#!/usr/bin/node
// Generates a rectangle class with height and width
module.exports = class Rectangle {
  // Constructors | Attribute Generators
  constructor (width, height) {
    if (width > 1 && height > 1) {
      this.width = width;
      this.height = height;
    }
  }

  // Triggers the print function
  print () {
    let buffer = '';

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) { buffer += 'X'; }
      if (i !== this.height - 1) { buffer += '\n'; }
    }
    console.log(buffer);
  }
};
