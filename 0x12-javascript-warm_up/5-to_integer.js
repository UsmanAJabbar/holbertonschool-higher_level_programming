#!/usr/bin/node
// Takes a number as input and returns it
!isNaN(process.argv[2]) ? console.log('My number: ' + parseInt(process.argv[2])) : console.log('Not a number');
