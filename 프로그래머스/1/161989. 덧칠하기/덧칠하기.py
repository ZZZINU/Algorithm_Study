def solution(n, m, section):
    answer = 0
#     paint_list = [True] * (n+1)
    
#     for item in section:
#         paint_list[item] = False
    
#     print(paint_list)
    start = section[0]
    
    for i in range(1, len(section)):
        if section[i] - start >= m:
            start = section[i]
            answer += 1
    
            
    
        
    
    return answer + 1