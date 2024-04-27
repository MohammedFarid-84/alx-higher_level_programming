#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  list.forEach((element) => {
    if (searchElement === element) {
      n++;
    }
  });
  return n;
};
