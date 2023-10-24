#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const resp = {};
    const json = JSON.parse(body);
    for (let n = 0; n < json.length; n++) {
      if (json[n].completed === true) {
        if (resp[json[n].userId] === undefined) {
          resp[json[n].userId] = 0;
        }
        resp[json[n].userId]++;
      }
    }
    console.log(resp);
  }
});
