#!/usr/bin/node
const request = require('request');
const fs = require('fs');
request(`${process.argv[2]}`, 'utf-8').pipe(fs.createWriteStream(process.argv[3]));

