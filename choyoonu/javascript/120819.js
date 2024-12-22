/* 프로그래머스 120819.아이스 아메리카노
(https://school.programmers.co.kr/learn/courses/30/lessons/120819) */

function solution(money) {
	var answer = [];
	const oneMoney = 5500;
	let firstResult = 1;
	let lastResult = 0;
	firstResult = Math.trunc(money / oneMoney);
	lastResult = money % oneMoney;
	answer.push(firstResult, lastResult);
	return answer;
}

