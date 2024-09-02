# 1949번: 우수 마을

# 런타임 에러 (RecursionError)가 떠서
# 재귀 깊이 한도를 크게 증가시켜야 함!
# Why? 
# RecursionError는 트리의 깊이가 깊어지면서 재귀 호출이 많아질 때 발생
# Python의 기본 재귀 한도인 1000을 초과하기 때문!
import sys
sys.setrecursionlimit(10**6) 

def dfs(cur):
    visited[cur] = 1 # 현재 마을을 방문했다고 표시

    # 현재 마을에 연결된 다른 마을들을 순회
    for current in tree[cur]: 

        # 만약 이웃 마을이 방문되지 않았다면
        if not visited[current]:
            # 이웃 마을에 대해 재귀적으로 DFS 실행
            dfs(current) 
            # 현재 마을이 우수 마을로 선정 O -> 이웃 마을은 우수 마을로 선정 X
            dp[cur][1] += dp[current][0] 
            # 현재 마을이 우수 마을로 선정 X -> 이웃 마을이 우수 마을로 선정 O or X 중에 최대값을 더한다
            dp[cur][0] += max(dp[current][0], dp[current][1])  
        
# N : 마을의 개수
N = int(input())

# 마을 주민 수 N개 입력
people = [0] + list(map(int, input().split()))

# tree 구성
tree = [[] for _ in range(N+1)]

# 마을 방문했는지 여부 파악
visited = [0 for _ in range(N+1)]

# DP 배열
# 각 마을에 대해 우수 마을로 선정했을 때 | 선정하지 않았을 때의 주민 수 저장
# [0, people[i]] : 선정 X
# [1, people[i]] : 선정 O
dp = [[0, people[i]] for i in range(N+1)]

# 마을 간의 연결 관계를 트리로 저장
for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 1번 마을부터 DFS 시작
dfs(1)

# 최댓값 출력
# 왜 1번 인덱스에서? -> 루트 노드니까 !
# 트리의 루트 노드를 기준으로 전체 트리에서 우수 마을을 선정했을 때의 최대 주민 수를 계산
print(max(dp[1][0], dp[1][1]))
