#!/usr/bin/node
exports.esrever = function (list) {
  const n = list.length;
  let lstElment;
  for (let i = 0; i < Math.floor(n / 2); i++) {
    lstElment = list[n - i];
    list[n - i] = list[i];
    list[i] = lstElment;
  }
};
