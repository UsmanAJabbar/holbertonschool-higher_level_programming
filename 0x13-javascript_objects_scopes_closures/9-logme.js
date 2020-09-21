#!/usr/bin/node
// Prints out strings and an index number
let index = 0;

exports.logMe = function (item) {
  console.log(index + ':', item);
  index += 1;
};
