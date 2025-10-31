from collections import deque
def solution(begin, target, words):
    
    def diff(a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
            
            if count > 1:
                return False
        else:
            return True


    
    q = deque([(begin, 0)])
    visited = []
    
    while q:
        word, step = q.popleft()
        if word == target:
            return step

        
        for w in words:

            if w not in visited and diff(w, word):
     
                q.append((w, step+1))
                visited.append(w)
            
                

    return 0