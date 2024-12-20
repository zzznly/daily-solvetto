function solution(emergency) {
    var answer = [];
    const sorted = [...emergency].sort((a,b) =>  b - a); 
    answer = emergency.map((v) => sorted.indexOf(v) + 1 );
    return answer;
}