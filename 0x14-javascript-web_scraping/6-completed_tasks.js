#!/usr/bin/node
const request = require('request');
let data;
const dictionary = {};
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in dictionary)) {
          dictionary[userid] = 0;
        }
        dictionary[userid] += 1;
      }
    });
    console.log(dictionary);
  }
});
