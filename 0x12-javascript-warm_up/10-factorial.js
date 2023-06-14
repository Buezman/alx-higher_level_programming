#!/usr/bin/node
const n = Math.floor(Number(process.argv[2]));

function factorial (n) {
  return (isNaN(n) || n === 0 ? 1 : n * factorial(n - 1));
}

console.log(factorial(n));
