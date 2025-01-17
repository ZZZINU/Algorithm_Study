def solution(n, lost, reserve):
    clothes = [1] * n
    answer = n
    
    for item in lost:
        clothes[item-1] = 0
    
    for item in reserve:
        clothes[item-1] += 1
    
    for i in range(n):
        if clothes[i] == 0:
            if i > 0 and clothes[i-1] == 2:
                clothes[i-1] -= 1
                clothes[i] = 1
            elif i < n-1 and clothes[i+1] == 2:
                clothes[i+1] -= 1
                clothes[i] = 1
        
    
    for cloth in clothes:
        if cloth == 0:
            answer -= 1
    
    return answer