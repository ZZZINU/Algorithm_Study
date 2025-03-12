function solution(x, n) {
    var answer = [];
    let count = 0;
    let start = x;
    while(count !== n) {
        answer.push(start)
        start += x;
        count += 1
    }
    

    return answer;
}