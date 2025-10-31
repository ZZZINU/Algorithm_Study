from collections import deque
def solution(n, results):
    
    G = [[] for _ in range(n+1)] # 승리 그래프 : A->B
    GR = [[] for _ in range(n+1)] # 역그래프 : B->A
    for a, b in results:
        G[a].append(b)
        GR[b].append(a)
    
    def bfs(start, graph):
        visited = [False] * (n+1)
        q = deque([start])
        visited[start] = True
        count = 0
        while q:
            cur = q.popleft()
            for item in graph[cur]:
                if not visited[item]:
                    visited[item] = True
                    q.append(item)
                    count += 1
        return count
            

    
    answer = 0
    for i in range(1, n+1):
        wins = bfs(i, G)
        losses = bfs(i, GR)
        
        if wins + losses == n-1:
            answer += 1
    
    return answer