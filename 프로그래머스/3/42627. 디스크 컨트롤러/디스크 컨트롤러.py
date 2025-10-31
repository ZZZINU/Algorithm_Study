import heapq

def solution(jobs):
    n = len(jobs)
    jobs = sorted([(s, l, i) for i, (s, l) in enumerate(jobs)])
    print(jobs)
    i=0
    t=0
    total_turn=0
    heap = []
    
    while i < n or heap:
        while i < n and jobs[i][0] <= t:
            s, l, idx = jobs[i]
            heapq.heappush(heap, (l, s, idx))
            i+=1
        
        if heap:
            l, s, idx = heapq.heappop(heap)
            t += l
            total_turn += t - s
        else:
            s, l, idx = jobs[i]
            t = max(t, s)
            heapq.heappush(heap, (l, s, idx))
            i+=1
            
    
    return total_turn // n