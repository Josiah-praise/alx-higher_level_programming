#!/usr/bin/node
const { argv } = require('node:process');

if (+argv[2]) {
  console.log(`My number: ${+argv[2]}`);
} else {
  console.log('Not a number');
}
