const input = require("fs")
  .readFileSync("../input.txt")
  .toString()
  .trim()
  .split("\n");
// const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, M] = input[0].split(" ").map(Number);
input.shift();
const space = input.map((inp) => {
  return inp.split(" ").map(Number);
});

const visit = Array.from(Array(N), () => Array(M).fill(0));
const dir = [
  [1, -1],
  [1, 0],
  [1, 1],
];
let res = Infinity;
const back = (r, c, d, subres) => {
  if (r === N - 1) {
    res = Math.min(subres, res);
    return;
  }
  for (let idx = 0; idx < 3; idx++) {
    const [dr, dc] = dir[idx];
    if (idx === d) {
      continue;
    }
    const nr = dr + r;
    const nc = dc + c;
    if (nr < 0 || nc < 0 || nr >= N || nc >= M || visit[nr][nc]) {
      continue;
    }
    visit[nr][nc] = 1;
    subres += space[nr][nc];
    back(nr, nc, idx, subres);
    visit[nr][nc] = 0;
    subres -= space[nr][nc];
  }
};
for (let i = 0; i < M; i++) {
  back(0, i, -1, space[0][i]);
}
console.log(res);

// 백트래킹 다음으로 보낼때 현재 방향을 보내서 그 방향은 못가게 처리
// space[0]의 모든 원소를 스타트지점으로 M개
// 종료조건은 행 인덱스가 N과 같을때 값 더해왔던거 min값 업데이트
