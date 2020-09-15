#!/usr/bin/node
// Prints the first argument passed to it
process.argv[2] !== undefined ? console.log(process.argv[2]) : console.log('No argument');
