# 9663번: N-Queen (🟡골드_4)
from itertools import combinations

N = int(input()) # N 입력

count = 0
row = [0] * N # 행

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
        
    return True


def queens(x):
    global count
    if x == N:
        count += 1
    
    else:
        for i in range(N):
            # [x, i]에 퀸 놓기
            row[x] = i
            if is_promising(x):
                queens(x+1)


queens(0)
print(count)
    
