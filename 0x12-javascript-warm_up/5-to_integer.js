#!/usr/bin/node

function conInt () {
  const args = process.argv[2];
  const num = parseInt(args);

  if (!isNaN(num)) {
    console.log(num);
  } else {
    console.log('Not a number');
  }
}

conInt();
