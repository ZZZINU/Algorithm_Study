from collections import deque
def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]
    
    answer = []
    n = len(maps)
    m = len(maps[0])
    
    new_maps = []
    
    for map in maps:
        temp = []
        for text in map:
            if text == 'X':
                temp.append(-1)
            else: 
                temp.append(int(text))
        new_maps.append(temp)
        

    
    # print(n, m)
    visited = [[False] * m for _ in range(n)]
    # print(visited)
    
    for i in range(n):
        for j in range(m):
            
            if new_maps[i][j] == -1 or visited[i][j]:
                continue
            
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            count = 0

            
            while q:
                
                x, y = q.popleft()
                count += new_maps[x][y]
                
                for e in range(4):
                    nx = dx[e] + x
                    ny = dy[e] + y
                    
                    if 0 <= nx < n and 0 <= ny < m:
                        if not visited[nx][ny] and new_maps[nx][ny] != -1:
                            q.append((nx, ny))
                            visited[nx][ny] = True
            answer.append(count)     
        answer.sort()
        
    return answer if answer else [-1]