#!/usr/bin/node
let arg1 = Math.floor(Number(process.argv[2]));
if (isNaN(arg1)) {
  console.log('Missing number of occurences');
} else {
  while (arg1 > 0) {
    console.log('C is fun');
    arg1--;
  }
}
