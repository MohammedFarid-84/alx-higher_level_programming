#!/usr/bin/node

const args = process.argv[2];
const num = parseInt(args);
let coulm, i = 0;

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (i = 0; i < num; i++) {
    coulm += 'X';
  }
  for (i = 0; i < num; i++) {
    console.log(coulm);
  }
}
