#!/usr/bin/node

exports.converter = function (base) {
  function doer(num) {
    if (Math.floor(num / base) === 0) {
      return (num % base).toString();
    } else {
      const mod = num % base;
      const quocient = Math.floor(num / base);
      return doer(quocient) + mod.toString();
    }
  }
  return doer;
};
