def solution(cap, n, deliveries, pickups):
    answer = 0
    need_d = 0
    need_p = 0
    
    for i in range(n-1, -1, -1):
        need_d += deliveries[i]
        need_p += pickups[i]
        
        while need_d > 0 or need_p >0:
            need_d -= cap
            need_p -= cap
            answer += (i+1) * 2
    
    return answer