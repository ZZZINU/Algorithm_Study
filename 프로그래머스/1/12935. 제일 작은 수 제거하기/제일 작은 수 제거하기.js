function solution(arr) {
    var arr_origin = arr.slice();
    var answer = [];
    if(arr.length == 1) {
        answer.push(-1)
    } else {
        arr.sort((a, b)=> a-b)
        let min = arr[0]
        for (let i=0;i<arr.length ; i++) {
            if (arr_origin[i] != min) {
                answer.push(arr_origin[i])
            }
            
        }
        
    }
    return answer;
}