import heapq

def solution(n, works):
    answer = 0
    
    if n >= sum(works):
        return answer
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)

    for work in works:
        answer += pow(work, 2)
    
    return answer