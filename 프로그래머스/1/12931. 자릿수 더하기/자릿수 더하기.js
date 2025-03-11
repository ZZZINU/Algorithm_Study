function solution(n)
{
    const digit = n.toString().split('');
    console.log(digit);
    const answer = digit.reduce((acc, digit) => acc + parseInt(digit), 0)

    return answer;
}