def solution(m, n, puddles):
    MOD = 1000000007
    answer = 0
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    puddle = set(map(tuple, puddles))
    
    # (x, y)
    for y in range(1, n+1):
        for x in range(1, m+1):
            print(x, y)
            if (x, y) in puddle:
                dp[y][x] = 0
                continue
            
            # 시작점
            if x == 1 and y == 1:
                continue 
            
            dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % MOD
                    

    
    return dp[n][m]