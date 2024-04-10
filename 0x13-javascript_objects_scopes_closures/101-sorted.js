#!/usr/bin/node

const { dict } = require('./101-data');
const newDict = {};

for (const i in dict) {
  if (dict[i] in newDict) {
    newDict[dict[i]].push(i);
  } else {
    newDict[dict[i]] = [i];
  }
}
console.log(newDict);
