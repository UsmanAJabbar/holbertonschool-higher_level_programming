#!/usr/bin/node
// Prints out the names of all the characters
// that played in a specific movie
const req = require('request');
let movieId = process.argv[2]
let endpoint = 'https://swapi-api.hbtn.io/api/films/' + movieId

if (!isNaN(movieId)) {
  req(endpoint, (err, res, jsonstr) => {
    let json = JSON.parse(jsonstr);
    let cast = [];

    for (CharacterEndpoint of json['characters']) {
      name_extractor(CharacterEndpoint);
    }
  });
}

function name_extractor (CharacterApiUrl) {
  req(CharacterApiUrl, (err, res, jsonstr) => {
    let json = JSON.parse(jsonstr);

    console.log(json['name']);
  });
}
