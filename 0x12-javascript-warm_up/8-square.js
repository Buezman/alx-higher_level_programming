#!/usr/bin/node
const arg1 = Math.floor(Number(process.argv[2]));
if (isNaN(arg1)) {
  console.log('Missing size');
} else {
  let n = arg1;
  while (n > 0) {
    console.log('X'.repeat(arg1));
    n--;
  }
}
