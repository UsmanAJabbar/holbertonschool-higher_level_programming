#!/usr/bin/node
// Prints the title of a specific Star Wars
// film found on the custom API https://swapi-api.hbtn.io/
const req = require('request');
const end = process.argv[2];

if (end !== undefined) {
  req(end, function (err, res, body) {
    err = !(err) ? console.log(corgi(JSON.parse(body))) : console.log(err);
  });
}

/**
 * corgi - this cute prototype of a wabbit
 * is about to sniff out how many times a
 * character was found in the custom API, end
 * @json: json object as input
 * Return: number of times character was found
 */
function corgi (json) {
  const size = json.results.length;
  let count = 0;

  for (let index = 0; index < size; index++) {
    for (let jindex = 0; jindex < json.results[index].characters.length; jindex++) {
      if (json.results[index].characters[jindex].includes('18')) {
        count += 1;
      }
    }
  }
  return count;
}
