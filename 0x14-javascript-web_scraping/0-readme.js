#!/usr/bin/node
// Reads and prints the contents of a file

const filename = process.argv[2];
const fs = require('fs');

fs.readFile(filename, 'utf8', function (err, data) {
  data = (err) ? console.log(err) : console.log(data);
});
