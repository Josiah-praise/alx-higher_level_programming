#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class extends Rectangle {
  constructor (side) {
    super(side, side);
  }
};
