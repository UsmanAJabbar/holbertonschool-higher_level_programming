#!/usr/bin/node
// Reverses a list, because that's what's cool now
exports.esrever = function (list) {
  const rev = [];
  for (let index = list.length - 1; index >= 0; index--) {
    rev.push(list[index]);
  }
  return rev;
};
