from collections import deque
def solution(maps):
    answer = 0
    q = deque()
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = True
    
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0 
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                # count += 1 # 이게 아니라
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
            
    if maps[n-1][m-1] == 1:
        answer = -1
    else:
        answer = maps[n-1][m-1]
    return answer