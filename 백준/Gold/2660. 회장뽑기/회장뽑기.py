# 2660번: 회장뽑기
N = int(input())
INF = float('inf')

dp = [[INF] * (N+1) for _ in range(N+1)] 

while True:
    a, b = map(int, input().split())

    if a == -1 and b == -1:
        break

    dp[a][b] = 1
    dp[b][a] = 1

# 자기 자신에서 자기 자신으로 가는 비용은 0
for i in range(1, N+1):
    dp[i][i] = 0

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

# 각 회원의 점수 계산 (최장 거리)
scores = [0] * (N+1)
for i in range(1, N+1):
    scores[i] = max(dp[i][1:])

# 회장 후보 점수 (최소의 최장 거리)
min_score = min(scores[1:])

result = []
for i in range(1, N+1):
    if scores[i] == min_score:
        result.append(i)

# 출력
# 회장 후보의 점수 | 후보의 수
# 회장 후보를 오름차순으로
print(min_score, len(result))
for i in result:
    print(i, end=" ")
