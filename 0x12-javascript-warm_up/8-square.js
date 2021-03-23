#!/usr/bin/node
let square = '';
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    for (let y = 0; y < parseInt(process.argv[2]); y++) {
      square += 'X';
    }
    if (x < parseInt(process.argv[2]) - 1) {
      square += '\n';
    }
  }
  console.log(square);
}
