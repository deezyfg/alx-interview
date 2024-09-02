#!/usr/bin/node
/**
 * Module to fetch and display Star Wars characters from a specific film.
 */
const util = require('util');
const request = util.promisify(require('request'));
const filmId = process.argv[2];

/**
 * Fetch and print the names of characters from a Star Wars film.
 * @param {string} filmId - The ID of the film to fetch characters from.
 */
async function starwarsCharacters(filmId) {
  try {
    const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
    let response = await request(endpoint);
    response = JSON.parse(response.body);
    const characters = response.characters;

    for (let i = 0; i < characters.length; i++) {
      const urlCharacter = characters[i];
      let character = await request(urlCharacter);
      character = JSON.parse(character.body);
      console.log(character.name);
    }
  } catch (error) {
    console.error('Error fetching data:', error);
  }
}

starwarsCharacters(filmId);
