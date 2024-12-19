function solution(age) {
    var answer = '';
    const alphabet = [];
    let alphabetNum = '';
    let age1, age2, age3, stringNum, num;
    for(let i = 97; i <= 106; i++ ){
        alphabetNum = String.fromCharCode(i);
        alphabet.push(alphabetNum);
        
    }
    
    answer = String(age).split('').map(num => alphabet[Number(num)]).join('');
    return answer;
}