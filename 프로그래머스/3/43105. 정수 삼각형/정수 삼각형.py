def solution(triangle):
    answer = 0
    dp = triangle[0][:]
    print(dp)
    for i in range(1, len(triangle)):
        row = triangle[i]
        new = [0] * (i+1)
        
        # 양끝
        new[0] = row[0] + dp[0]
        new[i] = row[-1] + dp[-1]
        
        for j in range(1, i):
            new[j] = row[j] + max(dp[j-1], dp[j])
        
        dp = new
        
        
        
    return max(dp)