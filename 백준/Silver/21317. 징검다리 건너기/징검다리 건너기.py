# 21317번: 징검다리 건너기(⚪실버_1)

N = int(input()) # 돌의 개수 N 입력
energy = []

for i in range(N-1):
    temp = list(map(int, input().split()))
    energy.append(temp)

K = int(input()) # 매우 큰 점프 에너지 K 입력

if N == 1:
    print(0)
elif N==2:
    print(energy[0][0])
else:
    dp = [0] * N
    dp[1] = energy[0][0]
    dp[2] = min(energy[0][0] + energy[1][0], energy[0][1])

    for i in range(3, N):
        dp[i] = min(dp[i-2] + energy[i-2][1], dp[i-1]+energy[i-1][0])

    result = dp[-1]
    dp2=dp[:]

    for i in range(0, N-3):
        if dp[i] + K < dp[i+3]:
            dp2[i+3] = dp[i]+K
            for j in range(i+4, N):
                dp2[j] = min(dp[j], dp2[j-1]+energy[j-1][0], dp2[j-2]+energy[j-2][1])
            if dp2[-1] < result:
                result = dp2[-1]

    print(result)


