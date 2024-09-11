def find_factor(num):
    
    nums = []
    
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            nums.append(i)
            nums.append(num // i)
    return nums

def solution(brown, yellow):
    
    answer = []
    count = brown + yellow
    factors = find_factor(yellow)
    
    for i in range(0, len(factors), 2):
        width = factors[i]
        height = factors[i+1]
        
        if (width + height) * 2 + 4 == brown:
            answer.append(height + 2)
            answer.append(width + 2)
            break
    
    return answer