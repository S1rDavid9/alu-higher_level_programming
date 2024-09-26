#!/usr/bin/node

// Import required modules
const fs = require('fs');

// Retrieve file paths from command line arguments
const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

// Read the contents of the first file
const data1 = fs.readFileSync(file1, 'utf-8');

// Read the contents of the second file
const data2 = fs.readFileSync(file2, 'utf-8');

// Concatenate the content of both files and write it to the destination file
fs.writeFileSync(destination, data1 + data2);
