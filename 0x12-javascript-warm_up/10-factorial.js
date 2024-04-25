#!/usr/bin/node

const num = parseInt(process.argv[2]);
function calcFact (no) {
  if (isNaN(no) || no === 0 || no === 1) {
    return 1;
  } else {
    return (no * calcFact(no - 1));
  }
}
console.log(calcFact(num));
