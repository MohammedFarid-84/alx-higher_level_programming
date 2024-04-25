#!/usr/bin/node
exports.callMeMoby = function callFnc (x, theFunction) {
  let i = 0;
  for (i = 0; i < x; i++) {
    theFunction();
  }
};
