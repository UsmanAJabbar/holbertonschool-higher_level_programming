#!/usr/bin/node
// Prints the title of a specific Star Wars
// film found on the custom API https://swapi-api.hbtn.io/
const req = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/';
const FilmID = process.argv[2];
const endpoint = api + FilmID;

if (FilmID !== undefined) {
  req(endpoint, function (err, res, body) {
    JSON.parse(body).title = !(err) ? console.log(JSON.parse(body).title) : console.log(err);
  });
}
