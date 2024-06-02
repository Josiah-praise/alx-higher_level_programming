#!/usr/bin/node
// https://hellosalut.stefanbohacek.dev/?lang=fr

$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: function (response) {
      $('div#hello').text(response.hello);
    },
    error: function (xhr, status, error) {
      console.log(`Error code: ${status}`);
    }
  });
});
