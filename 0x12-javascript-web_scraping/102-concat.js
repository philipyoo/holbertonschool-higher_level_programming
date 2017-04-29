#!/usr/bin/node
var fs = require('fs');

let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];

if (!fileA || !fileB || !fileC) {
  console.log('nope');
} else {
  [fileA, fileB].forEach((f) => {
    fs.readFileSync(f).toString().trim().split('\n').forEach((line) => {
      fs.appendFileSync(fileC, line.toString() + '\n');
    });
  });
}
