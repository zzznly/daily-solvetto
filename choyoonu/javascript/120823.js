/* 프로그래머스 120823.직각삼각형 출력하기
(https://school.programmers.co.kr/learn/courses/30/lessons/120823) */

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
	input = line.split(" ");
}).on("close", function () {
	let inputNum = Number(input[0]);
	for (let i = 1; i <= inputNum; i++) {
		console.log("*".repeat(i));
	}
});