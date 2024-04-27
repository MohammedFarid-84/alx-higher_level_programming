#!/usr/bin/node
let alredyPrinted = 0;

exports.logMe = function (item) {
  const txt = alredyPrinted + ': ' + item;
  console.log(txt);
  alredyPrinted += 1;
};
