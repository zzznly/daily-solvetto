const input = `
4
DOG
GOD
GOOD
DOLL
DO
`
  .toString()
  .trim()
  .split("\n");

// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')
const N = input[0];
const stan = input[1];
const words = input.slice(2);
let result = 0;

for (let word of words) {
  if (
    Math.abs(stan.length - word.length) > 1 ||
    Math.abs(new Set(stan).size - new Set(word).size) > 1
  ) {
    continue;
  }

  for (const char of stan) {
    word = word.replace(char, "");
  }
  if (word.length < 2) {
    result++;
  }
}
console.log(result);
