def solution(participant, completion):
    answer = ''
    hash_map = {}
    
    for person in completion:
        if person not in hash_map:
            hash_map[person] = 1
        else:
            hash_map[person] += 1
            
    for person in participant:
        if person not in hash_map:
            return person
        
        if person in hash_map:
            if hash_map[person] == 0:
                return person
            else:
                hash_map[person] -= 1
                
            
        
        
    
    return answer