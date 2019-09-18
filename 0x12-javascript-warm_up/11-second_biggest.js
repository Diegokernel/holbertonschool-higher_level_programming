#!/usr/bin/node

const num = process.argv;
if (num.length > 3) {
  console.log(num.sort((a, b) => b - a).slice(3)[0]);
} else {
  console.log(0);
}
