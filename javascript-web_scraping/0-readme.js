#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];

// Check if the file path argument is provided
if (!filePath) {
  console.error('Usage: ./read_file.js <file_path>');
  process.exit(1);
}

// Read the file using fs.readFile
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    // If an error occurs, log the error
    console.error(err);
    return;
  }
  // Print the content of the file
  console.log(data);
});
