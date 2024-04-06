# 11728번: 배열 합치기 (⚪실버_5)
from collections import deque

N, M = map(int, input().split())

deque1 = deque(map(int, input().split()))
deque2 = deque(map(int, input().split()))

result = []

for i in range(N+M):
    if len(deque1) == 0 or len(deque2) == 0:
        result.extend(deque1)
        result.extend(deque2)
        break
    elif deque1[0] < deque2[0]:
        result.append(deque1.popleft())
    else :
        result.append(deque2.popleft())
    
print(" ".join(map(str, result)))