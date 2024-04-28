#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
  const value = dict[key];
  if (!newDict[value]) { newDict[value] = []; }
  if (newDict[value]) {
    newDict[value].push(key.toString());
  }
}
console.log(newDict);
