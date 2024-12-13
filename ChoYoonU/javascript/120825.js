/* 프로그래머스 120825.문자 반복 출력하기
(https://school.programmers.co.kr/learn/courses/30/lessons/120825) */

function solution(my_string, n) {
	var answer = "";
	answer = [...my_string];
	for (i = 0; i < answer.length; i++) answer[i] = answer[i].repeat(n);
	return answer.join("");
}