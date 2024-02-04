# 7576번: 토마토 (🟡골드_5)
from collections import deque # deque를 사용하기 위해 라이브러리 사용

# 방문하지 않은 1을 찾는 함수
def find_one(tomato):
    # 토마토의 정보가 1이고 방문하지 않은 곳이라면 인덱스를 저장
    index = [(i, j) for i, row in enumerate(tomato) for j, element in enumerate(row) if element == 1 and visited[i][j]==0]
    
    # 저장한 인덱스 반환
    return index

# 토마토를 익히는 함수
def ripe_tomato(i, j):
    visited[i][j] = 1 # 해당 인덱스는 방문한 것으로 처리

    # 상하좌우에 대해서 MxN을 넘어가지 않고 방문하지 않았다면
    # 상하좌우에 대해서 토마토를 익히고
    # 상하좌수에 대해서 방문한 것으로 처리하고
    # next_ones에 해당 인덱스를 추가 -> 그 인덱스를 기준으로 익히기 위해서

    # 상
    if i - 1 >= 0 and tomato[i-1][j]==0 and visited[i-1][j]==0:
        tomato[i-1][j] = 1
        visited[i-1][j] = 1
        next_ones.append((i-1, j))
    
    # 하
    if i + 1 < N and tomato[i+1][j]==0 and visited[i+1][j]==0:
        tomato[i+1][j] = 1
        visited[i+1][j] = 1
        next_ones.append((i+1, j))
    
    # 좌
    if j - 1 >= 0 and tomato[i][j-1]==0 and visited[i][j-1]==0:
        tomato[i][j-1] = 1
        visited[i][j-1] = 1
        next_ones.append((i, j-1))
    
    # 우
    if j + 1 < M and tomato[i][j+1]==0 and visited[i][j+1]==0:
        tomato[i][j+1] = 1
        visited[i][j+1] = 1
        next_ones.append((i, j+1))

# 토마토가 다 익었는지 체크하는 함수
def check_ripen(tomato, visited):

    # 모든 칸을 검사
    for i in range(N):
        for j in range(M):
            # 토마토 정보가 0인데(익지 않음) 방문한 적이 없다면 -> -1에 가로막혀서 익지 못한 토마토
            if tomato[i][j] == 0 and visited[i][j] == 0:
                return False  # 따라서 다 익지 않았음 -> False 반환
    return True # 다 익었다면 True 반환


tomato = [] # 토마토의 정보 저장
count = 0 # 날짜 저장

M, N = map(int, input().split()) # 상자의 크기 입력

# 토마토의 정보 입력
for i in range(N):
    temp = list(map(int, input().split()))
    tomato.append(temp)

# 방문 유무 저장 
# 0: 방문 X , 1: 방문 O
visited = [[0] * M for _ in range(N)]

next_ones = deque(find_one(tomato)) # 방문하지 않은 1 있는 부분 인덱스 추출해서 저장

# next_ones이 있다면 반복 
while next_ones:
    count += 1 # next_ones이 있다는 것은 익을 토마토가 있다는 것! 따라서 하루 +1 증가
    size = len(next_ones) 
    for _ in range(size): # 1의 개수만큼 반복
        i, j = next_ones.popleft() # 1의 인덱스를 pop()
        ripe_tomato(i, j) # 저장한 인덱스 기준으로 토마토 익히기

# 토마토가 다 있었는지 체크
if check_ripen(tomato, visited):
    print(count-1) # 다 익었다면 날짜 출력 -> -1을 하는 이유: 마지막 토마토는 이미 다 익었는데 한번더 체크를 하기 때문에
else:
    print(-1) # 다 안 익었다면 -1 출력