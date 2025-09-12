def solution(arr):
    answer = []
    for one in arr:
        if answer:
            if one != answer[-1]:
                answer.append(one)
        else:
            answer.append(one)
                
            
    return answer