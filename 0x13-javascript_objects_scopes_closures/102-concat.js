#!/usr/bin/node
const filesAry = process.argv[2];
const fs = require('fs');

if (filesAry !== undefined) {
  for (let i = 2; i < 4; i++) {
    const fileName = process.argv[i];
    const data = fs.readFileSync(fileName, 'UTF-8');

    if (data.charCodeAt(0) === 0xFEFF) {
      data = data.substr(1);
    }
    if (i < 3) {
      fs.writeFileSync(process.argv[4], data);
    } else {
      fs.appendFileSync(process.argv[4], data);
    }
  }
}
