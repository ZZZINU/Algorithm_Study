def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    first_score = 0
    second_score = 0
    third_score = 0
    
    for i in range(len(answers)):
        dap = answers[i]
        if first[i%5] == dap:
            first_score += 1
        if second[i%8] == dap:
            second_score += 1
        if third[i%10] == dap:
            third_score += 1
        
    max_score = max(first_score, second_score, third_score)
    if max_score == first_score:
        answer.append(1)
    if max_score == second_score:
        answer.append(2)
    if max_score == third_score:
        answer.append(3)
    
    
        
    
    return answer