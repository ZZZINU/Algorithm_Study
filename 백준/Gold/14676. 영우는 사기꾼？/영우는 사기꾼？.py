# 14676번: 영우는 사기꾼?
# 건물 종류의 개수 N
# 건물 사이 관계의 개수 M
# 영우의 게임 정보의 개수 K
N, M, K = map(int, input().split())

# building : 건물의 관계
# building[i] : i 건물을 지어야 지을 수 있는 건물들 
building = [[] for _ in range(N+1)]
indegree = [0] * (N+1) # 진입차수

# 건물의 관계 입력
for i in range(M):
    X, Y = map(int, input().split())
    building[X].append(Y) # X 건물을 지어야 지을 수 있는 건물 Y
    indegree[Y] += 1 # Y 건물의 진입차수 +1

# 새롭게 건물 건설 | 파괴
new_building = []

# 게임 정보의 개수만큼 반복
for i in range(K):
    X, Y = map(int, input().split())
    if X == 1: # 1은 건설
        # 진입차수가 0인 경우
        if indegree[Y] == 0:
            # Y 건물이 이미 건설된 적 있는지 파악 -> 진입차수를 중복으로 감소시키는 것을 방지
            if Y not in new_building:
                # Y 건물을 선수로 하는 건물들의 진입 차수를 감소
                for b in building[Y]:
                    if indegree[b] > 0:
                        indegree[b] -= 1
            # 건물 건설
            new_building.append(Y)
        
        # 진입차수가 0이 아닌데 건물을 건설하려고 했다면 -> 치트키
        else:
            print("Lier!")
            exit()
    
    else: # 2는 파괴
        # 건물이 건설된 적 있는지 파악 -> 파괴
        if Y in new_building:
            new_building.remove(Y) 
            # 건물이 하나도 없다면 이 건물을 선수로 하는 건물들의 진입차수 +1 증가
            if Y not in new_building:
                for b in building[Y]:
                    indegree[b] += 1
        # 건물이 없는데 파괴하려고 한다면 -> 치트키
        else:
            print("Lier!")
            exit()

print("King-God-Emperor")