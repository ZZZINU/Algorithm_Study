# 13164번: 행복 유치원

N, K = map(int, input().split())

kindergartner = list(map(int, input().split()))

diff = []

for i in range(1, N):
    diff.append(kindergartner[i] - kindergartner[i-1])

diff.sort()

if K > 1:
    print(sum(diff[:-(K-1)]))
else:
    print(sum(diff))
