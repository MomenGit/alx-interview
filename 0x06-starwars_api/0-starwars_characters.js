#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer
const request = require('request');
const process = require('process');

request.get(
  `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`,
  (err, res, body) => {
    if (err) console.log(err);
    else {
      const charactersUrls = JSON.parse(body).characters;
      charactersUrls.forEach((url) => {
        request.get(url, (err, res, body) => {
          if (!err) console.log(JSON.parse(body).name);
        });
      });
    }
  }
);
