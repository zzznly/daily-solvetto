/* 프로그래머스 120817.배열의 평균값
(https://school.programmers.co.kr/learn/courses/30/lessons/120817) */

function solution(numbers) {
	var answer = 0;
	const sumNumbers = numbers.reduce((accumulator, currentValue) => accumulator + currentValue);
	answer = sumNumbers / numbers.length;
	return answer;
}

