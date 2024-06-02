#!/usr/bin/node
// fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    type: 'GET',
    success: function (response) {
      $('div#character').text(response.name);
    },
    error: function (xhr, status, error) {
      console.log('Error');
    }
  });
});
