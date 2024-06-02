#!/usr/bin/node
// fetches and prints how to say “Hello” depending on the language

$(document).ready(function () {
  $('input#btn_translate').click(function () {
    // get the language code
    const langCode = $('input#language_code').val();
    // api endpoint
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

    const success = function (response) {
      $('div#hello').text(response.hello);
    };

    const error = function (xhr, status, error) {
      console.log(`Error code: ${status}`);
    };
    const type = 'GET';

    $.ajax({ url, success, type, error });
  });
});
