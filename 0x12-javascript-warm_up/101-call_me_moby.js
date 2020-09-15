#!/usr/bin/node
// Takes in parameters and prints them out
exports.callMeMoby = function (n, print) {
  for (let index = 0; index < n; index++) { print(); }
};
