#!/usr/bin/node

let arg = process.argv[2];
if (arg == null) {
  console.log('No argument');
} else {
  console.log(arg);
}
