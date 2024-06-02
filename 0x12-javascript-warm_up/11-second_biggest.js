#!/usr/bin/node

const { argv } = require('node:process');

let arr = argv.filter((x) => !isNaN(+x));
arr = arr.map((x) => +x);

if (arr.length <= 1) {
  console.log(0);
} else {
  let largest = arr[0];
  let secondLargest;
  for (const i of arr) {
    if (i > largest) {
      secondLargest = largest;
      largest = i;
    } else if (i > secondLargest && i !== largest) {
      secondLargest = i;
    }
  }
  console.log(secondLargest);
}
