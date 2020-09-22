#!/usr/bin/node
// Prints out the names of all the characters
// that played in a specific movie
const req = require('request');
const movieId = process.argv[2];
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;

if (!isNaN(movieId)) {
  req(endpoint, (err, res, jsonstr) => {
    const json = JSON.parse(jsonstr);

    for (var CharacterEndpoint of json.characters) {
      name(CharacterEndpoint);
    }
  });
}

function name (CharacterApiUrl) {
  req(CharacterApiUrl, (err, res, jsonstr) => {
    const json = JSON.parse(jsonstr);
    console.log(json['name']);
  });
}
