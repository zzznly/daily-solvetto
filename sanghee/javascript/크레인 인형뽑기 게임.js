function solution(board, moves) {
  let count = 0;
  const box = [];

  for (const move of moves) {
    for (const row of board) {
      const item = row[move - 1];

      if (item !== 0) {
        count = pickItem(item, box, count);
        row[move - 1] = 0;
        break;
      }
    }
  }

  return count;
}

function checkBox(box, count) {
  if (box.length < 2) return count;
  if (box.at(-1) === box.at(-2)) {
    box.splice(-2, 2);
    return count + 2;
  }
  return count;
}

function pickItem(item, box, count) {
  box.push(item);
  return checkBox(box, count);
}
