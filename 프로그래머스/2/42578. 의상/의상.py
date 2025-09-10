def solution(clothes):
    
    hash_map = {}
    for cloth in clothes:
        cloth_name, cloth_type = cloth
        if cloth_type in hash_map:
            hash_map[cloth_type].append(cloth_name)
        else:
            hash_map[cloth_type] = [cloth_name]
            
    if len(hash_map) == 1:
        return len(clothes)
    
    answer = 1
    for key in hash_map:
        answer *= (len(hash_map[key]) + 1)
    

        
        
    return answer - 1