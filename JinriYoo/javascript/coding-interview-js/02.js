// 문제 02 - 배열 제어하기
// 정수 배열을 하나 받아서, 중복값 제거하고 내림차순으로 정렬

const solution = (arr) => {
    const newArr = [...new Set(arr)];
    return newArr.sort((a, b) => b - a);
}


console.log(solution([4, 2, 2, 1, 3, 4])); // [4, 3, 2, 1]
console.log(solution([2, 1, 1, 3, 2, 5, 4])); // [5, 4, 3, 2, 1]
