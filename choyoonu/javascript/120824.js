/* 프로그래머스 120824.짝수 홀수 개수
(https://school.programmers.co.kr/learn/courses/30/lessons/120824) */

function solution(num_list) {
	var answer = [];
	let a = 0; // 짝수 개수
	let b = 0; // 홀수 개수
	for (let i = 0; i < num_list.length; i++) {
		if (num_list[i] % 2 == 0) {
			a++;
		} else {
			b++;
		}
	}
	answer = [a, b];

	return answer;
}