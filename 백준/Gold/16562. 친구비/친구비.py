
# 16562번: 친구비
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, A,  x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if A[rootX] < A[rootY]:
            parent[rootY] = rootX
        else:
            parent[rootX] = rootY

N, M, k = map(int, input().split())
parent = list(range(N))

A = list(map(int, input().split()))

for i in range(M):
    x, y = map(int, input().split())
    union(parent, A, x-1, y-1)
# 각 노드에 대해 최종 대표자(root)를 찾음
for i in range(N):
    parent[i] = find(parent, i)

# 대표자별 최소 비용을 계산
min_cost = {}
for i in range(N):
    root = parent[i]
    if root in min_cost:
        min_cost[root] = min(min_cost[root], A[i])
    else:
        min_cost[root] = A[i]

# 총 비용 계산
total = sum(min_cost.values())

    
total = 0
for item in set(parent):
    total += A[item]

if total > k:
    print("Oh no")
else:
    print(total)