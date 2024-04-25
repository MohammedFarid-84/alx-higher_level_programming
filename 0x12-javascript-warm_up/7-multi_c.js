#!/usr/bin/node

const x = process.argv[2];
const y = parseInt(x);
let i = 0;

if (isNaN(y)) {
    console.log('Missing number of occurrences');
} else {
    for (i = 0; i < y; i++) {
        console.log('C is fun');
    }
}