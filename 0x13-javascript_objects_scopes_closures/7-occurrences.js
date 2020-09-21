#!/usr/bin/node
// Finds the number of occurrences
// a specific int/string appears in a list
exports.nbOccurences = function (list, searchElement) {
  let count = 0; let elements;

  for (elements of list) {
    (elements === searchElement) ? count += 1 : {};
  }
  return count;
};
