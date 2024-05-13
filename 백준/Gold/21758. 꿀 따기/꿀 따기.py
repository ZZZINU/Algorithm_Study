# 21758번: 꿀 따기
N = int(input())
honey = list(map(int, input().split()))

# 최댓값 
max_honey = 0

# i번째 원소까지의 누적합
sum = []
sum.append(honey[0])

for i in range(1, N):
    sum.append(sum[i-1] + honey[i])

# 가장 오른쪽에 꿀통
for i in range(1, N-1):
    max_honey = max(max_honey, sum[N-1] - honey[0] - honey[i] + sum[N-1] - sum[i])


# 가장 왼쪽에 꿀통
for i in range(1, N-1):
    max_honey = max(max_honey, sum[N-2] - honey[i] + sum[i-1])



# 가운데에 꿀통
for i in range(1, N-1):
    max_honey = max(max_honey, sum[N-2] - honey[0] + honey[i])

print(max_honey)