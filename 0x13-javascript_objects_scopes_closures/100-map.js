#!/usr/bin/node
const list = require('./100-data.js').list;
const map = list.map((n, idx) => n * idx);
console.log(list);
console.log(map);
