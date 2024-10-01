#!/usr/bin/node

// Import the required module
const fs = require('fs');

// Retrieve the file path from command line arguments
const filePath = process.argv[2];

// Read the file content in utf-8 format
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurs, print the error object
    console.log(err);
  } else {
    // Print the content of the file
    console.log(data);
  }
});
