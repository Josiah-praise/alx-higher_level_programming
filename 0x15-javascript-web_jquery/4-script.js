#!/usr/bin/node
// toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header

$(function () {
  $('div#toggle_header').click(function () {
    $('header').toggleClass('red');
    $('header').toggleClass('green');
  });
});
