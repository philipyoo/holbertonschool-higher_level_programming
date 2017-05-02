#!/usr/bin/node
const request = require('request');

request('http://swapi.co/api/people/5/?format=json', (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  $('DIV#character').text(JSON.parse(body).name);
});
