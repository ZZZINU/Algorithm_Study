from itertools import permutations

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    
    data = list(numbers)
    cases = []
    for i in range(1, len(numbers)+1):
        temp = list(set(permutations(data, i)))
        while temp:
            case = ''.join(temp.pop())
            cases.append(int(case))
    
    cases = list(set(cases))
    
    for num in cases:
        if is_prime(num):
            answer += 1

    
    return answer