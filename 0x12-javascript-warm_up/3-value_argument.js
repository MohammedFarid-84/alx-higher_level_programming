#!/usr/bin/node

const args = process.argv.slice(2);
let x = 0;

args.forEach((val, index) => {
  if (val !== null) {
    console.log(`${val}`);
    x += 1;
  }
});

if (x === 0) {
  console.log('No argument');
}
