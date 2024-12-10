function ranking(count) {
  let rank;
  if (count === 6) rank = 1;
  else if (count === 5) rank = 2;
  else if (count === 4) rank = 3;
  else if (count === 3) rank = 4;
  else if (count === 2) rank = 5;
  else rank = 6;

  return rank;
}

function counting(lottos, win_nums) {
  let count = 0;
  let zeroCount = 0;

  lottos.forEach((number) => {
    if (win_nums.includes(number)) count++;
    if (!number) zeroCount++;
  });

  return [count, zeroCount];
}

function solution(lottos, win_nums) {
  const [count, zeroCount] = counting(lottos, win_nums);
  return [ranking(count + zeroCount), ranking(count)];
}
