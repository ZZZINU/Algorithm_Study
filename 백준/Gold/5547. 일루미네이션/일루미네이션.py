# 5547번: 일루미네이션 
from collections import deque

w, h = map(int, input().split())
graph = [[0 for _ in range(w+2)] for _ in range(h+2)]
for i in range(1, h+1): # 높이 설정
    graph[i][1:w+1] = map(int, input().split())

dy = [0, 1, 1, 0, -1, -1]
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]] # y가 짝수인 경우, 홀수인 경우

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    visited = [[False for _ in range(w+2)] for _ in range(h+2)] # 방문 여부
    visited[y][x] = True
    count = 0
    while queue:
        y, x = queue.popleft()

        for i in range(6):
            yy = y + dy[i]
            if y % 2 == 0: # 짝수인 경우
                xx = x+dx[0][i]
            else: # 홀수인 경우
                xx = x+dx[1][i]
            
            if 0 <= yy < h+2 and 0 <= xx < w+2:
                if graph[yy][xx] == 0 and not visited[yy][xx]:
                    queue.append((yy, xx))
                    visited[yy][xx] = True
                elif graph[yy][xx] == 1:
                    count += 1
    return count

print(bfs(0,0))