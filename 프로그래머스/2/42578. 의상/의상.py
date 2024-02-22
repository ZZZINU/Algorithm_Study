def solution(clothes):
    
    clothes_sort = {}
    for i in range(len(clothes)):
        if clothes[i][1] in clothes_sort:
            clothes_sort[clothes[i][1]].append(clothes[i][0])
        else:
            clothes_sort[clothes[i][1]] = [clothes[i][0]]
    
    answer = 1
    for key, value in clothes_sort.items():
        answer *= (len(value) + 1)

    answer -= 1

        
    
    return answer