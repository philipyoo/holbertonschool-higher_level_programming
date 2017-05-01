#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(data);
});
