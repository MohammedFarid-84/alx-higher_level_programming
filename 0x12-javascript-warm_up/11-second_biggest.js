#!/usr/bin/node

let big = 0;
let bigs = 0;
const args = process.argv.slice(2);

args.forEach((element) => {
  element = parseInt(element);
  if (element > big) {
    bigs = big;
    big = element;
  }
});
console.log(bigs);
