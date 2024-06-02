#!/usr/bin/node
// adds, removes and clears LI elements from a list when the user clicks

$(function () {
  const parent = $('ul.my_list');
  const newElement = '<li>Item</li>';

  // When the user clicks on DIV#add_item
  $('div#add_item').click(function () {
    parent.append(newElement);
  });

  //   When the user clicks on DIV#remove_item
  $('div#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  // When the user clicks on DIV#clear_list
  $('div#clear_list').click(function () {
    $('ul.my_list > li').remove();
  });
});
