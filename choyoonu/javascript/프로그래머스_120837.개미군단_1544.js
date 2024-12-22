function solution(hp) {
    var answer = 0;
    let answer1 = 0;
    let answer2 = 0;
    let answer3 = 0;
    
    const a = 5;
    const b = 3;
    const c = 1;
    
    answer1 = Math.trunc(hp / a); 
    answer2 = Math.trunc((hp % a) / b);
    answer3 = ((hp % a) % b);
    answer =  answer1 + answer2 + answer3;
    
    return answer;
}