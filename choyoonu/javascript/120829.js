/* 프로그래머스 120829.각도기
(https://school.programmers.co.kr/learn/courses/30/lessons/120829) */

function solution(angle) {
	var answer = 0;
	if (angle == 180) {
		return (answer = 4);
	}
	if (angle > 90 && angle < 180) {
		return (answer = 3);
	}
	if (angle == 90) {
		return (answer = 2);
	}
	if (angle > 0 && angle < 90) {
		return (answer = 1);
	}
	return answer;
}
