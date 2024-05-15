from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
size = list(map(int, input().split()))


size_combi = list(combinations(size, 2))
case = []

# 기본 - 웍의 크기
for item in size:
    case.append(item)

# 조합 - 웍의 크기 조합
for item in size_combi:
    case.append(sum(item))

# 중복 제거
case = set(case)

# 최소 요리 횟수 저장
count = [0] * (N + 1)


for i in range(1, N+1): # i : 만들 숫자
    min_count = 100000000
    for item in case: # 경우의 수 - 한번에 요리할 수 있는 짜장면의 수 1, 3, 4 ...
        if i - item >= 0: # 경우의 수로 만들 수 있는 경우
            min_count = min(min_count, count[i - item] + 1)
    count[i] = min_count

if count [N] == 100000000:
    print(-1)
else:
    print(count[N])

