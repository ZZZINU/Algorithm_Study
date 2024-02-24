def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    
    length = len(answers)
    
    count = [0,0,0]
    
    for i in range(length):
        if person1[i % 5] == answers[i]:
            count[0] += 1
        if person2[i % 8] == answers[i]:
            count[1] += 1
        if person3[i % 10] == answers[i]:
            count[2] += 1
    
    for idx, score in enumerate(count):
        if max(count) == score:
            answer.append(idx+1)
    
    return answer