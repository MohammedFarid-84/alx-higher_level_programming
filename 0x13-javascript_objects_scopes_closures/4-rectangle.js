#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    let x = 'X';
    if (this.width > 0 && this.height > 0) {
      for (let i = 1; i < this.width; i++) {
        x = x + 'X';
      }
      for (let i = 0; i < this.height; i++) {
        console.log(x);
      }
    }
  }

  rotate () {
    const w = this.width;
    this.width = this.height;
    this.height = w;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
