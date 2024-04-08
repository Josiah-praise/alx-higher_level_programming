#!/usr/bin/node

const { argv } = require('node:process');

const factorial = (num) => {
  if (isNaN(num)) {
    return 1;
  } else if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
};

console.log(factorial(+argv[2]));
