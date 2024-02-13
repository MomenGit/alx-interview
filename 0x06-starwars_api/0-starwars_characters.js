#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const process = require('process');

const movieId = process.argv[2];

function fetchCharacters (characterUrls, index) {
  if (index >= characterUrls.length) return;

  request.get(characterUrls[index], (err, res, body) => {
    if (err) return;
    const character = JSON.parse(body);
    console.log(character.name);
    fetchCharacters(characterUrls, index + 1);
  });
}

request.get(
  `https://swapi-api.alx-tools.com/api/films/${movieId}`,
  (err, res, body) => {
    if (err) console.log(err);
    else {
      const charactersUrls = JSON.parse(body).characters;
      fetchCharacters(charactersUrls, 0);
    }
  }
);
