#!/usr/bin/node
// Reads content from the terminal and writes it to
// a specified file

const filename = process.argv[2]
const content = process.argv[3]
const fs = require('fs')

fs.writeFile(filename, content, 'utf8', function (err, data) {
  data = (err) ? console.log(err) : {}
})
