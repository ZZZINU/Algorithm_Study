# 1647번: 도시 분할 계획
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX < rootY:
        parent[rootY] = rootX
    else:
        parent[rootX] = rootY

N, M = map(int, input().split())

edges = []
parent = [num for num in range(N+1)]

for i in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()
answer = 0
answer_list = []

for edge in edges:
    cost, A, B = edge
    if find(parent, A) != find(parent, B):
        union(parent, A, B)
        answer += cost
        answer_list.append(cost)

print(answer - answer_list[-1])




