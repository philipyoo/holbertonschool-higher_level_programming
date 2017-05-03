#!/usr/bin/node
const request = require('request');

request('http://swapi.co/api/films?format=json', (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  let data = JSON.parse(body).results;
  for (let i = 0; i < data.length; i++) {
    $('ul#list_movies').append('<li>' + data[i].title + '</li>');
  }
});
