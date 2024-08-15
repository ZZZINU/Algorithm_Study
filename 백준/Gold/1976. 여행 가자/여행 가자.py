# 1976번: 여행 가자
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        parent[rootY] = rootX

N = int(input())
M = int(input())
link = []
plan = []

# 부모
parent = list(range(N))

for i in range(N):
    temp = list(map(int, input().split()))
    link.append(temp)
    for j in range(N):
        if temp[j] == 1:
            union(parent, i, j)

# 여행 계획 입력
plan = list(map(int, input().split()))

# 1) 첫 번째 도시의 루트를 찾고, 
# 2) 모든 도시가 같은 루트에 속하는지 확인
root = find(parent, plan[0]-1)

for i in range(1, M):
    if find(parent, plan[i]-1) != root:
        print("NO")
        exit()

print("YES")


