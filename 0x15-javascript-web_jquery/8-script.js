#!/usr/bin/node
// fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    success: function (response) {
      response.results.forEach(function (item) {
        $('ul#list_movies').append(`<li>${item.title}</li>`);
      });
    },
    error: function (xhr, status, error) {
      console.log(`Error code ${status}`);
    }
  });
});
