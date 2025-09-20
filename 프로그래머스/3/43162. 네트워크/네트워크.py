def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    for s in range(n):
        if visited[s]:
            continue
        answer += 1
        stack = [s]
        visited[s] = True
        
        while stack:
            i = stack.pop()
            for j in range(n):
                if computers[i][j] == 1 and not visited[j]:
                    stack.append(j)
                    visited[j] = True
    
    

    
    
    return answer