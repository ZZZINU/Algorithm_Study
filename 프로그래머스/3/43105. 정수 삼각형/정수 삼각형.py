def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = triangle[0]
    
    for i in range(1, n):
        dist = triangle[i]
        
        dist[0] += dp[0]
        dist[-1] += dp[-1]
        
        for j in range(1, len(dist)-1):
            dist[j] += max(dp[j-1], dp[j])
        
        dp = dist
    
    print(dp)
    
    return max(dp)