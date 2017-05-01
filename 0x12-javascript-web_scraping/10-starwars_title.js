#!/usr/bin/node
const request = require('request');

const episodeId = process.argv[2];

if (parseInt(episodeId) < 8) {
  const url = 'http://swapi.co/api/films/' + episodeId;

  request(url, (err, res, body) => {
    if (err) {
      return console.log(err);
    }
    console.log(JSON.parse(body).title);
  });
}
