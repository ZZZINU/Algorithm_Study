from collections import defaultdict
def solution(n, computers):
    answer = 0
    tree = defaultdict(list)
    # 연결먼저
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                continue
            
            if computers[i-1][j-1] == 1:
                tree[i].append(j)
    
    visited = [False] * n
    
    for i in range(1, n+1):
        
        if visited[i-1]:
            continue
        
        stack = [i]
        visited[i-1] = True
        
        while stack:
            node = stack.pop()
            if node in tree:
                for item in tree[node]:
                    if not visited[item-1]:
                        stack.append(item)
                        visited[item-1] = True
        
        answer += 1
        
            
        
    
    return answer