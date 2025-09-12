import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for one in scoville:
        heapq.heappush(heap, one)
    
    while len(heap) > 1:
        one = heapq.heappop(heap)
        
        if one >= K:
            return answer
        
        two = heapq.heappop(heap)
        new = one + (two * 2)
        answer += 1
        heapq.heappush(heap, new)
    
    if heapq.heappop(heap) >= K:
        return answer
    
    
    return -1