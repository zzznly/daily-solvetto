// 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/92334

// 구하고 싶은 것. 각 유저별로 처리 결과 메일을 받은 횟수
// 구하기 위해 필요한 것
// 각 유저별로 처리 결과 메일 횟수가 담긴 배열, answer
// 신고 당한 유저-신고당한 유저들의 객체, reportedUser
// 얘네들을 카운트할 객체, count
function solution(id_list, report, k) {
  const reportedUser = {};
  const count = {};
  const answer = [];

  for (let r of report) {
    const [reportId, reportedId] = r.split(" ");
    if (!reportedUser[reportedId]) {
      //중복된 유저를 카운트하지 못하게 set으로
      reportedUser[reportedId] = new Set();
    }
    reportedUser[reportedId].add(reportId);
  }

  for (let reportedId of Object.keys(reportedUser)) {
    //k번 이상 신고된 유저는 메일 발송 -> 카운트 대상이 됨
    if (reportedUser[reportedId].size >= k) {
      for (let id of reportedUser[reportedId]) {
        count[id] = (count[id] || 0) + 1;
      }
    }
  }

  for (let i = 0; i < id_list.length; i++) {
    answer.push(count[id_list[i]] || 0);
  }

  return answer;
}
