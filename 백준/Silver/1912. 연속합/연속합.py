n = int(input())
num = list(map(int, input().split()))

max_sum = -1000
dp = [0] * n  

for i in range(n):
    if i == 0:
        dp[i] = num[i]
    else:
        dp[i] = max(dp[i - 1] + num[i], num[i])

    if dp[i] > max_sum:
        max_sum = dp[i]

print(max_sum)
