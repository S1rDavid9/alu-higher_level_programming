#!/usr/bin/node

// Import the dictionary from 101-data.js
const dict = require('./101-data').dict;

// Create a new dictionary to hold occurrences as keys and user ids as values
const newDict = {};

// Iterate over the dict object
for (const userId in dict) {
  const occurrences = dict[userId];

  // If the occurrences number is not a key in newDict, add it
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }

  // Push the userId into the list for that occurrence
  newDict[occurrences].push(userId);
}

// Print the new dictionary
console.log(newDict);
