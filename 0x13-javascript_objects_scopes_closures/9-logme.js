#!/usr/bin/node

function closure () {
  const arr = [0];
  return (string) => {
    console.log(`${arr[0]}: ${string}`);
    arr[0]++;
  };
}

exports.logMe = closure();
