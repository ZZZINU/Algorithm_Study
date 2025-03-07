function solution(left, right) {
    var answer = 0;
    for(let i=left;i<=right;i++){
        console.log(i);
        var count = 1;
        for (let j=2; j<=i; j++) {
            if(i % j == 0) {
                count += 1
            }
        }
        if (count % 2 == 0) {
            answer += i
        } else {
            answer -= i
        }
        
    }
    return answer;
}