/* 프로그래머스 120826.특정 문자 제거하기
(https://school.programmers.co.kr/learn/courses/30/lessons/120826) */

function solution(my_string, letter) {
	var answer = "";
	answer = my_string.replaceAll(letter, "");
	return answer;
}