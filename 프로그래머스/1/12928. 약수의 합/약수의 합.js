function solution(n) {
    var answer = n;
    if (n > 1){
        answer += 1
    }
    
    for(let i = 2 ; i < n ;  i++) {
        if (n % i == 0) {
            answer += i
        }
        
    }
 
    return answer;
}