#!/usr/bin/node

module.exports.nbOccurences = function (list, searchElement) {
  const filteredList = list.filter((x) => x === searchElement);
  return filteredList.length;
};
