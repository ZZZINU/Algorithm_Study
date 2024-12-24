def solution(name, yearning, photo):
    answer = []
    score = {}
    
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    for photo_one in photo:
        count = 0
        for person in photo_one:
            if person in score:
                count += score[person]
        answer.append(count)    
        
        
    
    return answer