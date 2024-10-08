from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    border = [[-1] * 102 for i in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    border[i][j] = 0
                elif border[i][j] != 0:
                    border[i][j] = 1 # 테두리 체크
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    q = deque()
    q.append([characterX * 2, characterY * 2])
    visited = [[1] * 102 for i in range(102)] # 1: 방문 X
    visited[characterX * 2][characterY * 2] = 0
    
    while q:
        x, y = q.popleft()
        
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if border[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return answer