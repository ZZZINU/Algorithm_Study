from collections import defaultdict
def solution(n, computers):
    answer = 0
    hash_map = defaultdict(list)
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and computers[i-1][j-1] == 1:
                hash_map[i].append(j)
    

    visited = [False] * (n+1)
    
    for i in range(1, n+1):
        stack = []
        if visited[i]:
            continue
        answer += 1
        stack.append(i)
        visited[i] = True
        
        while stack:
            now = stack.pop()

            for item in hash_map[now]:
                if not visited[item]:
                    stack.append(item)
                    visited[item] = True
                
        
    
            
            
        
        
    
    return answer