#!/usr/bin/node

const { argv } = require('node:process');

let arr = argv.filter((x) => !isNaN(+x));
arr = arr.map((x) => +x);

if (arr.length <= 1) {
  console.log(1);
} else {
  console.log(arr.sort().at(-2));
}
