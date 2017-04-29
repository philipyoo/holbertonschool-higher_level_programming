#!/usr/bin/node
var fs = require('fs');

var file = process.argv[2] || "";

fs.readFile(file, 'utf8', function(err, data) {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(data);
});
