#!/usr/bin/node
const fs = require('request');
fs(process.argv[2], (err, res) => {
  if (err) return console.log(err);
  console.log('code: %d', res.statusCode);
});
