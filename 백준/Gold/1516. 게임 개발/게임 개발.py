# 1516번: 게임 개발
from collections import deque

# 건물의 개수 입력
N = int(input())

# 각 건물에 대한 정보를 저장할 리스트를 초기화
# building[i] : i번 건물을 짓기 위해 먼저 지어야 하는 건물들
building = [[] for _ in range(N+1)]

# indegree[i]는 i번 건물을 짓기 위해 먼저 지어야 하는 건물들의 개수 -> 진입차수
indegree = [0] * (N+1) 

# 각 건물의 건설 시간을 저장
cost = [0] * (N+1)

# 각 건물의 건설 시간, 먼저 지어야 하는 건물들의 정보 입력
for i in range(1, N+1):
    data = list(map(int, input().split()))[:-1] # 마지막 -1 빼고
    cost[i] = data[0] # data의 첫 번째 값은 i번 건물의 건설 시간
    building_data = data[1:] # 나머지 값들은 먼저 지어야하는 건물들

    # 먼저 지어야 하는 건물들 순회 -> 그래프와 진입차수 설정
    for j in building_data:
        building[j].append(i) # j번 건물을 짓고 나서, i번 건물을 지을 수 있음
        indegree[i] += 1 # 진입차수 증가

# 위상 정렬 함수
def topology_sort():
    # 최종적으로 각 건물이 완성되는 시간을 저장
    result = [0] * (N+1) 
    q = deque()

    # 진입차수가 0인 건물들을 큐에 추가
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft() # 큐에서 하나의 건물을 꺼내기
        result[now] += cost[now] # 현재 건물의 건설 시간 추가

        # 현재 건물 이후에 지을 수 있는 건물들을 순회
        for b in building[now]:
            indegree[b] -= 1 # 해당 건물의 진입차수 하나 줄이기
            # 이전 건물의 최종 건설 시간을 반영해 현재 건물의 건설 시간을 업데이트
            result[b] = max(result[b], result[now])

            # 진입차수가 0이 되면 큐에 추가
            if indegree[b] == 0:
                q.append(b)

    # 모든 건물의 최종 건설 시간을 반환
    return result

# 위상 정렬을 통해 각 건물의 최종 건설 시간을 계산하고 출력
answer = topology_sort()
for i in range(1, N+1):
    print(answer[i])
