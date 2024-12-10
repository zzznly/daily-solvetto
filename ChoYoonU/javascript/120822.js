/* 프로그래머스 120822.배열 뒤집기
(https://school.programmers.co.kr/learn/courses/30/lessons/120822) */

function solution(my_string) {
	var answer = "";
	answer = my_string.split("").reverse().join("");
	return answer;
}
