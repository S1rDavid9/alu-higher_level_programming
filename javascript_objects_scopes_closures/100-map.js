#!/usr/bin/node

// Import the list from 100-data.js
const list = require('./100-data').list;

// Compute the new list using map and multiply each value by its index
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
