#!/usr/bin/node

const Parent = require('./5-square');

class Square extends Parent {
  charPrint (c) {
    let square = '';
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        square += c !== undefined ? c : 'X';
      }
      if (y < this.height - 1) {
        square += '\n';
      }
    }
    console.log(square);
  }
}

module.exports = Square;
