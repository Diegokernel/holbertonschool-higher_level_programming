#!/usr/bin/node

const val = process.argv[2];
if (Number(val)) {
    for (let a = 0; a < val; a++) {
	console.log('X'.repeat(val));
    }
} else {
    console.log('Missing size');
}
