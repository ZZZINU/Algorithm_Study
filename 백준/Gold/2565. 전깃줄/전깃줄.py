# 2565번: 전깃줄
N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()


dp = [1] * N

for i in range(N): # 현재 전깃줄
    for j in range(i): # 현재 전깃줄 이전에 있는 전깃줄들
        if lines[i][1] > lines[j][1]: # 현재 전깃줄의 끝점 > 이전 전깃줄의 끝점 => 
            dp[i] = max(dp[i], dp[j]+1) # dp 업데이트 -> 이전 전깃줄까지의 길이 + 현재 전깃줄을 추가한 길이 VS 현재까지의 길이

print(N - max(dp))