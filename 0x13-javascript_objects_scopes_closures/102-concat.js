#!/usr/bin/node
const filesAry = process.argv[2];
const fs = require('fs');

if (filesAry !== undefined) {
    for (let i = 2; i < 4; i++) {
      const fileName = process.argv[i];
      //console.log(fileName);
      const data = fs.readFileSync(fileName, 'utf-8')
      fs.writeFileSync(filesAry[2], data);
    }
}
