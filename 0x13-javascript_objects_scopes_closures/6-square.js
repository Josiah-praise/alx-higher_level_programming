#!/usr/bin/node

const Rectangle = require('./5-rectangle');

module.exports = class Square extends Rectangle {
  charPrint (char = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
};
