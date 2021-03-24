#!/usr/bin/node
exports.esrever = function (list) {
  const final = list.length - 1;
  const arr = [];
  for (let i = final; i >= 0; i--) {
    arr.push(list[i]);
  }
  return (arr);
};
