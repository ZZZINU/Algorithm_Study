def solution(triangle):

    n = len(triangle)
    dp = []
    dp.append(triangle[0][0])


    for i in range(1, n):
        dist = triangle[i]

        dist[0] += dp[0] 
        dist[-1] += dp[-1] 
        
        for j in range(1, i):
            dist[j] += max(dp[j-1], dp[j])
        
        dp = dist
        
    
    
    return max(dist)