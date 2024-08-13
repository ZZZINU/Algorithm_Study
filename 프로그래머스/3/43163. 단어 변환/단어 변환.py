from collections import deque

def solution(begin, target, words):
    if target not in words:
        answer = 0
    else:
        queue = deque()
        queue.append([begin, 0])
        
        while queue:
            now, step = queue.popleft()
            
            if now == target:
                answer = step
                return answer
            
            for word in words:
                count = 0
                for i in range(len(now)):
                    if now[i] != word[i]:
                        count += 1
                    
                if count == 1:
                    queue.append([word, step + 1])
                    
    
    return answer