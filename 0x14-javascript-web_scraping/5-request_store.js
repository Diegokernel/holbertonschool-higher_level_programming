#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body).results;
    let n = 0;
    for (const i in film) {
      for (const j in film[i].characters) {
        if (film[i].characters[j].includes('18')) {
          n++;
        }
      }
    }
    console.log(n);
  }
});
