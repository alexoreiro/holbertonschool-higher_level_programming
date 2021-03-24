#!/usr/bin/node
let total = 0;
exports.logMe = function (item) {
  const print = total + ': ' + item;
  console.log(print);
  total++;
};
