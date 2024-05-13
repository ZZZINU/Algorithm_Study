# 2217번: 로프
N = int(input())


weight = []
for i in range(N):
    weight.append(int(input()))

weight.sort()

max_num = 0

for i in range(1, N+1):
    max_num = max(max_num, i * weight[-i])

print(max_num)

