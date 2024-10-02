#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

// Check if both arguments (file path and content) are provided
if (!filePath || !content) {
  console.error('Usage: ./write_file.js <file_path> <string_to_write>');
  process.exit(1);
}

// Write the string to the file using fs.writeFile
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // If an error occurs, log the error
    console.error(err);
    return;
  }
  console.log('File written successfully');
});

