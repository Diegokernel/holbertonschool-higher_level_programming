#!/usr/bin/node

const args = process.argv;
const n1 = parseInt(args[2]);
const n2 = parseInt(args[3]);

function add (a, b) {
  return (a + b);
}
console.log(add(n1, n2));
