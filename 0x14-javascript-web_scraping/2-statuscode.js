#!/usr/bin/node
// Returns the status code after pinging a GET
// request at a specific URL.
const req = require('request');
const endpoint = process.argv[2];

req(endpoint, function (err, res, body) {
  res.statusCode = !(err) ? console.log('code:', res.statusCode) : {};
});
