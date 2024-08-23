def solution(answers):
    result= []
    answer = [0, 0, 0]
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == person1[i%5]:
            answer[0] += 1
        if answers[i] == person2[i%8]:
            answer[1] += 1
        if answers[i] == person3[i%10]:
            answer[2] += 1
    
    max_val = max(answer)
    for idx, item in enumerate(answer):
        if item == max_val:
            result.append(idx+1)
        
        
    return result