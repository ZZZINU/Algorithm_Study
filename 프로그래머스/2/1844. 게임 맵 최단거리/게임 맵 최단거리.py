from collections import deque
def solution(maps):
    answer = 1
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
  

    
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == False:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                visited[nx][ny] = True
                
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    

    return answer
