import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        answer += 1
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        res = one + (two * 2)
        heapq.heappush(scoville, res)
    
    return answer