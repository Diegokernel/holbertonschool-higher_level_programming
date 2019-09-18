#!/usr/bin/node

function factorial (n) {
    if (n > 1) {
	return factorial(n - 1) * n;
    }
    else { return 1; }
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
