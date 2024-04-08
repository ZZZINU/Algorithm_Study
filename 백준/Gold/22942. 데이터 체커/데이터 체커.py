from sys import stdin
N = int(input())

circle = []
stack = []

for i in range(N):
    x, r = map(int, stdin.readline().split())
    circle.append([x-r, x, 0])
    circle.append([x+r, x, 1])

circle.sort()

for i in range(N * 2):
    if circle[i][2] == 0: # 원의 왼쪽 좌표라면
        stack.append(circle[i][1])
    elif circle[i][2] == 1:
        if circle[i][1] == stack.pop():
            continue
        else:
            print("NO")
            exit(0)

print("YES")
