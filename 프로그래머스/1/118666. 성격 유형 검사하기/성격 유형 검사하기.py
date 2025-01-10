def solution(survey, choices):
    personality = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    dict = {}
    answer = ''
    
    for person in personality:
        dict[person] = 0
    
    for i in range(len(survey)):
        first = survey[i][0]
        second = survey[i][1]

        if choices[i] < 4:
            dict[first] += 4 - choices[i]
        elif choices[i] > 4:
            dict[second] += choices[i] - 4 
    
    
    for i in range(4):
        if dict[personality[i*2]] >= dict[personality[i*2+1]]:
            answer += personality[i*2]
        else:
            answer += personality[i*2+1]
        
        
    
    return answer


