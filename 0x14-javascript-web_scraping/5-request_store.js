#!/usr/bin/node
// Fetches the content from a URL specified in
// the terminal saves the content to a file defined
// by the terminal
const fs = require('fs')
const req = require('request')
const end = process.argv[2]
const filename = process.argv[3]

if (end && filename) {
  req(end, function (err, res, body) {
    fs.writeFile(filename, body, 'utf8', function (err, data) {
      data = (err) ? console.log(err) : {};
    });
  }
)}
