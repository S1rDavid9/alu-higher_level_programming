#!/usr/bin/node
// 7-occurrences.js
exports.nbOccurences = function (list, searchElement) {
  let count = 0;

// Loop through the list
  for (let i = 0; i < list.length; i++) {
// If the current element matches the searchElement, increment the count
    if (list[i] === searchElement) {
      count++;
    }
  }

  return count;
};
