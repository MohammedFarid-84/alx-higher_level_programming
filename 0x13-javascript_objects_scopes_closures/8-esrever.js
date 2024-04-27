#!/usr/bin/node
exports.esrever = function (list) {
  const n = list.length;
  const x = Math.floor(n / 2);
  for (let i = 0; i < x; i++) {
    const lstElment = list[n - (i + 1)];
    list[n - (i + 1)] = list[i];
    list[i] = lstElment;
  }
  return list;
};
