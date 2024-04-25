#!/usr/bin/node

let num = parseInt(process.argv[2]);
let x = 0;
function calcFact (no) {
  if (isNaN(no) || no === 0 || no === 1) {
    return 1;
  } else {
    return (no * calcFact(no - 1));
  }
}
x = calcFact(num);
console.log(x);
