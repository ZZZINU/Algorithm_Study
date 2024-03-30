# 9465번: 스티커(⚪실버_1)

result = []


T= int(input())

for _ in range(T):
    n = int(input())
    dp = []
    
    # 스티커 점수 2차원 배열로
    for i in range(2):
        temp = list(map(int, input().split()))
        dp.append(temp)
    
    # n = 1인 경우
    if len(dp[0]) == 1:
        print(max(dp[0][0], dp[1][0]))
        # result.append(max(dp[0][0], dp[1][0]))
    else:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        
        for i in range(2,n):
            dp[0][i] += max(dp[1][i-1], dp[1][i-2])
            dp[1][i] += max(dp[0][i-1], dp[0][i-2])
        
        print(max(dp[0][n-1], dp[1][n-1]  ))
