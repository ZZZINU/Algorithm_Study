def solution(nums):
    answer = 0
    count = len(nums) / 2
    num_set = set(nums)
    
    if count <= len(num_set):
        return count
    else:
        return len(num_set)
    
    

        
    
    
    return answer