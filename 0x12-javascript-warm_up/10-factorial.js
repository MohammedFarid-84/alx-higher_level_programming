#!/usr/bin/node

const num = parseInt(process.argv[2]);
let i = 1;
let fact = 1;

for (i = 1; i <= num; i++) {
  fact *= i;
}
console.log(fact);
