#!/usr/bin/node
const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (let index = 0; index < results.length; index++) {
      for (let char = 0; char < results[index].characters.length; char++) {
        if (results[index].characters[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
