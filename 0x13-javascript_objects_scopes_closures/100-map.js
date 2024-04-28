#!/usr/bin/node
const list = require('./100-data').list;
let num = 0;

const facor = list.map((elem) => {
  return elem * num++;
});
console.log(list);
console.log(facor);
