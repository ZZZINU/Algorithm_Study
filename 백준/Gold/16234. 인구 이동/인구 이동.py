# 16234번: 인구 이동 (🟡골드_5)
from collections import deque # deque를 위해 라이브러리 사용

# [N: 땅 크기, L: 인구 차이 최소, R: 인구 차이 최대] 입력
N, L, R = map(int, input().split())

A = [] # 각 나라의 인구 수 저장

# 각 나라의 인구 수 입력
for i in range(N):
    temp = list(map(int, input().split()))
    A.append(temp)

# 상,하,좌,우에 대한 x,y 좌표 방향 벡터를 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 국경선을 공유하고 있는 나라를 반환하는 함수
def bfs(a, b):
    queue = deque() # 현재 위치에서 이동 가능한 위치 저장 (=탐색할 좌표)
    temp = [] # 국경선을 공유하고 있는 나라 저장
    
    # 현재 좌표 추가
    queue.append((a, b))
    temp.append((a, b))
    
    # 현재 위치에서 이동 가능한 위치가 있다면
    while queue:
        x, y = queue.popleft() # 좌표 추출

        # 상하좌우 = 총 4번 반복
        for i in range(4):
            Nx = x + dx[i] # x 좌표 설정
            Ny = y + dy[i] # y 좌표 설정
            
            # 해당 좌표가 땅 크기에서 벗어나지 않고, 아직 방문하지 않았다면
            if 0<=Nx<N and 0<=Ny<N and visited[Nx][Ny] == 0:
                # 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면
                if L <= abs(A[x][y]-A[Nx][Ny]) <= R:
                    visited[Nx][Ny] = 1 # 방문했음으로 처리
                    queue.append((Nx, Ny)) # 이동 가능한 위치에 추가
                    temp.append((Nx, Ny)) # 국경선을 공유하고 있는 나라에 추가
                    
    return temp # 국경선을 공유하고 있는 나라 반환


result = 0 # 인구 이동이 며칠 동안 발생하는지 저장

# 더 이상 인구이동이 일어나지 않을 때(flag==0) 까지 반복
while True:
    visited = [[0] * (N+1) for _ in range(N+1)] # 방문 여부 저장
    flag = 0 # 인구 이동 여부 판단 (0이면 인구이동 x, 1이면 인구이동 o)
    
    # 모든 나라에 대해서 반복
    for i in range(N):
        for j in range(N):
            if visited[i][j]==0: # 해당 나라를 아직 방문하지 않았다면
                visited[i][j]=1 # 방문했음으로 표시
                country = bfs(i, j) # 해당 인덱스의 나라에 대해서 국경선을 공유하는 나라 추출
                
                # 국경선을 공유하고 있는 나라가 1보다 크다면(자기 자신빼고 하나 이상 있으면)
                if len(country) > 1:
                    flag = 1 # 인구 이동 o
                    # 연합을 이루고 있는 각 칸의 인구수 : (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
                    number = sum([A[x][y] for x, y in country]) // len(country)
                    # 연합 인구 수 바꾸기
                    for x,y in country:
                        A[x][y] = number
    # 더 이상 인구이동이 일어나지 않는다면                    
    if flag == 0:
        break # 반복문 종료

    result += 1 # while문이 한번 돌 때마다(인구 이동 한번 일어날 때 마다) 1씩 증가

print(result) # 인구 이동이 며칠 동안 발생하는지 출력