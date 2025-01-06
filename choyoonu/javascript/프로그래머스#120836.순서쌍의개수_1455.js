function solution(n) {
    var answer = 0;
    let resultN = 0;
    
    for(i = 1 ; i <= n ; i++){
        if(n % i == 0 ) {
            resultN++;
            answer = resultN;
        }  
         
    }
        
    return answer;
}