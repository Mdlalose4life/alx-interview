#!/usr/bin/node

// Imporing the request library
const request = require('request');

// Defining and assigning the starwars URL
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if the number of command line arguments is greater than 2
if (process.argv.length > 2) {
  // Requesting a film based on the ID
  request(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    // Log the error occured during the request
    if (err) {
      console.log(err);
    }
    // Get charachter from fil's body
    const charactersURL = JSON.parse(body).characters;

    // Creating a series of Promises that resolve with the names of the characters
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        // Make a request to the character resource
        request(url, (promiseErr, __, charactersReqBody) => {
          // Reject the request if an error occure, during the request
          if (promiseErr) {
            reject(promiseErr);
          }
          // Othewise resolve the promise, with the number of characters
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    // wait for all promises to be resolve, log all characters and separate them with new lines
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}

