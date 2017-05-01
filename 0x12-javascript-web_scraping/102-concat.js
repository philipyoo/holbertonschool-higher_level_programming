#!/usr/bin/node
const fs = require('fs');

let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];

try {
  [fileA, fileB].forEach((f) => {
    fs.readFileSync(f).toString().trim().split('\n').forEach((line) => {
      fs.appendFileSync(fileC, line.toString() + '\n');
    });
  });
} catch (err) {
  console.log(err);
}
