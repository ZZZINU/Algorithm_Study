from collections import deque
def solution(begin, target, words):
    answer = 0
    
    def can_change(word1, word2):
        count = 0
        for i in range(len(word1)):
            if count >= 2:
                return False
            
            if word1[i] != word2[i]:
                count += 1
                
        if count == 1:
            return True
        else:
            return False
    
    q = deque([(begin, 0)])
    visited = set([begin])
    
    while q:
        now, dist = q.popleft()
        if now == target:
            return dist
        
        for word in words:
            if word not in visited and can_change(word, now):
                visited.add(word)
                q.append((word, dist+1))
    
    
    return answer