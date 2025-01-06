from heapq import heappush, heappop

def solution(k, score):
    answer = []
    fame = [] # 명예의 전당
    
    for s in score:
        heappush(fame, s)
        if len(fame) > k:
            heappop(fame)
        answer.append(fame[0])
    
    return answer