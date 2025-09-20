from collections import deque

def differ_by_one(a, b):
    diff = 0
    for x, y in zip(a, b):
        if x != y:
            diff +=1
        if diff > 1:
            return False
    
    return diff == 1
        

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    q = deque()
    q.append((begin, 0)) # 현재 단어, 단계수
    visited = set([begin])
    
    while q:
        cur, step = q.popleft()
        if cur == target:
            return step
        
        for w in words:
            if w not in visited and differ_by_one(cur, w):
                visited.add(w)
                q.append((w, step+1))
    
    
    return answer