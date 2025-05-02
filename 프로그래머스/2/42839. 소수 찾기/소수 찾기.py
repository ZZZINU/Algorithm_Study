from itertools import permutations
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range (2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
            
        
    


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    
    length = len(numbers)
    check = []
    
    for i in range(1, length+1):
        temp = list(permutations(numbers, i))
        while temp:
            case = ''.join(temp.pop())
            check.append(int(case))
    
    check = list(set(check))
    
    for num in check:
        if is_prime(num):
            answer += 1
            
            
    
    

    
    return answer