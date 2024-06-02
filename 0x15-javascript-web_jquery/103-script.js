#!/usr/bin/node
// fetches and prints how to say “Hello” depending on the language

const handler = function () {
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
};

$(document).ready(function () {
  $('input#btn_translate').click(handler);
  $('input#language_code').keydown(function (event) {
    if (event.key === 'Enter') {
      handler();
    }
  });
});
