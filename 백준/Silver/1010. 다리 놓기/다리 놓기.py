# 1010번: 다리놓기
from itertools import combinations

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == j:
                dp[i][j] = 1
            
            elif i == 1:
                dp[i][j] = j
            
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
            
    print(dp[i][j])
