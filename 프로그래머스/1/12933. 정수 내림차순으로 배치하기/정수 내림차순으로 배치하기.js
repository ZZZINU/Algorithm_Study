function solution(n) {

    let n_string = n.toString();
    console.log(n_string);
    let split = Array.from(n_string);
    console.log(split.sort().reverse());
    split = split.sort().reverse();
    
    var answer = Number(split.join(''));
    return answer;
}