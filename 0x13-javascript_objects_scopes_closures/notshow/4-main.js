#!/usr/bin/node

const Rectangle = require('./4-rectangle');

console.log('Normal:');
const r1 = new Rectangle(2, 3);
r1.print();

console.log('Double:');
r1.double();
r1.print();

console.log('Rotate:');
r1.rotate();
r1.print();
