#!/usr/bin/node
// Converts a number from base 10
exports.converter = function (base) {
  return function parser (input) {
    return input.toString(base);
  };
};
