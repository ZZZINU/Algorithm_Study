def solution(participant, completion):
    answer = ''
    roster = {}
    for person in participant:
        if person not in roster:
            roster[person] = 1
        else:
            roster[person] += 1
    
    for person in completion:
        roster[person] -= 1
    
    for person in roster:
        if roster[person] != 0:
            answer += person
    
    
    return answer