#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const FileA = fs.readFileSync(args[2]).toString();
const FileB = fs.readFileSync(args[3]).toString();

fs.appendFile(args[4], FileA + FileB, function (err) {
  if (err) throw err;
});
