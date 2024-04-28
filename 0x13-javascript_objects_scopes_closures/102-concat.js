#!/usr/bin/node
const filesAry = process.argv[2];
const fs = require('fs');

if (filesAry !== undefined) {
    for (let i = 0; i < 2; i++) {
      const fileName = filesAry[i];
      const data = fs.readFileSync(fileName, 'utf-8')
      fs.writeFileSync(filesAry[2], data);
    }
}
