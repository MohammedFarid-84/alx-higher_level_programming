#!/usr/bin/node
const S = require('./5-square');

class Square extends S {
  charPrint (c) {
    let cr = 'X';
    if (c !== undefined) {
      cr = c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(cr.repeat(this.width));
    }
  }
}
module.exports = Square;
