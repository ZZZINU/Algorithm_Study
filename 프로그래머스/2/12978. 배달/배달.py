import heapq
def solution(N, road, K):
    answer = 0
    
    # 1. 인접 리스트 구성
    graph = [[] for _ in range(N+1)]
    for a, b, w in road:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    # 2. 거리 배열 초기화
    INF = float('inf')
    dist = [INF] * (N+1)
    dist[1] = 0
    
    # 3. 우선순위 큐 (현재까지 시간, 정점)
    pq = [(0, 1)]
    while pq:
        cur_time, u = heapq.heappop(pq)
        
        # 이미 더 짧은 경로로 방문 했었다면 패스
        if cur_time > dist[u]:
            continue
        
        for v, w in graph[u]:
            new_time = cur_time + w
            if new_time < dist[v]:
                dist[v] = new_time
                heapq.heappush(pq, (new_time, v))
    
    
    for time in dist:
        if time <= K:
            answer += 1
    
        


    return answer