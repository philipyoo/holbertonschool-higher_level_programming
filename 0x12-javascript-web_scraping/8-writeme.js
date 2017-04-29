#!/usr/bin/node
var fs = require('fs');

const file = process.argv[2] || '';
const data = process.argv[3] || '';

fs.writeFile(file, data, (err) => {
  if (err) {
    return console.log(err);
  }
});
