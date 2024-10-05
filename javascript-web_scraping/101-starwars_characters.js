#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Array to hold all promises for fetching character names
    const characterPromises = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    });

    // Wait for all promises to complete and then print the character names
    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => console.log(name));
      })
      .catch(err => {
        console.error(err);
      });
  }
});
