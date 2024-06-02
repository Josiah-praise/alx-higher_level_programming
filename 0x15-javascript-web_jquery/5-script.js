#!/usr/bin/node
// adds a <li> element to a list when the user clicks on the tag DIV#add_item

$(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>item<li>');
  });
});
