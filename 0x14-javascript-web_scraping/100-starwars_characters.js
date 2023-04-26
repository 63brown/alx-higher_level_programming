#!/usr/bin/node
const request = require('request');
request.get(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    for (const key in JSON.parse(body).characters) {
      request.get(JSON.parse(body).characters[key], (error, response, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
