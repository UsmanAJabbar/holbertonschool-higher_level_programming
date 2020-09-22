#!/usr/bin/node
// Fetches the content from a URL specified in the
// terminal saves the content to a file defined by the terminal
const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const filename = process.argv[3];

if (url && filename) {
  req(url, function (err, res, body) {
    (err) ? console.log(err) : fs.writeFileSync(filename, body);
  });
}
