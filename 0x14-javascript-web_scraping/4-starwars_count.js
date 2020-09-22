#!/usr/bin/node
// Prints the title of a specific Star Wars
// film found on the custom API https://swapi-api.hbtn.io/
const req = require('request');
const end = 'https://swapi-api.hbtn.io/api/films/';
const characterid = process.argv[2];
const character = 'https://swapi-api.hbtn.io/api/people/' + characterid + '/';

if (characterid !== undefined) {
  req(end, function (err, res, body) {
    err = !(err) ? console.log(corgi(JSON.parse(body), character)) : console.log(err);
  });
}

/**
 * corgi - this cute prototype of a wabbit
 * is about to sniff out how many times a
 * character was found in the custom API, end
 * @character: character that needs to be found
 * Return: number of times character was found
 */
function corgi (body, character) {
  const size = body.results.length;
  let count = 0;

  for (let index = 0; index < size; index++) {
    count = (body.results[index].characters.includes(character)) ? count += 1 : count += 0;
  }
  return count;
}
