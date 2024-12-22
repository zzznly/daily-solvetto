function solution(want, number, discount) {
  let answer = 0;
  const total = number.reduce((acc, cur) => {
    return acc + cur;
  }, 0);

  for (let i = 0; i < discount.length - total + 1; i++) {
    const checkMap = new Map();
    for (let j = 0; j < total; j++) {
      const cur = checkMap.get(discount[i + j]) + 1 || 1;
      checkMap.set(discount[i + j], cur);
    }

    let flag = true;
    for (let k = 0; k < want.length; k++) {
      const cur = checkMap.get(want[k]);
      if (!cur) {
        flag = false;
        break;
      }
      if (cur !== number[k]) {
        flag = false;
        break;
      }
    }

    if (flag) {
      answer++;
    }
  }
  return answer;
}

// 9:15
// 9:36
