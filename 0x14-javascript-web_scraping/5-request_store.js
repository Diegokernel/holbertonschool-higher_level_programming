#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) console.log(error);
  fs.writeFile(process.argv[3], body, 'utf8', function (error) {
    if (error) console.log(error);
  });
});
