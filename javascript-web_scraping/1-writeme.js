#!/usr/bin/node
const fs = require('fs');

// Get the file path and the string from the command line arguments
const filePath = process.argv[2];
const text = process.argv[3];

// Write the string to the file
fs.writeFile(filePath, text, 'utf-8', (err) => {
  if (err) {
    console.log(err); // Print the error if one occurred
  }
});
