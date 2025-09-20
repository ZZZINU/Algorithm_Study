def solution(sequence, k):
    n = len(sequence)
    
    left = 0
    curr = 0
    
    best_len = float('inf')
    best = [0, 0]
    
    for right in range(n):
        curr += sequence[right]
        
        while curr >= k and left <= right:
            if curr == k:
                length = right - left + 1
                if length < best_len or (length == best_len and left < best[0]):
                    best_len = length
                    best = [left, right]
            
            curr -= sequence[left]
            left += 1
    
    
    
    return best