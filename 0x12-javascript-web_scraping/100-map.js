#!/usr/bin/node
let list = require('./100-data').list;

console.log(list);

list = list.map((n, i) => {
  return n * i;
});

console.log(list);
