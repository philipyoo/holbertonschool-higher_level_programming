#!/usr/bin/node
let dict = require('./101-data').dict;

let storage = {};

for (let item in dict) {
  if (!storage[dict[item]]) {
    storage[dict[item]] = [];
  }
  storage[dict[item]].push(item);
}

console.log(storage);
