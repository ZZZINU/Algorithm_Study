# 1922번: 네트워크 연결
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

N = int(input())
M = int(input())
parent = [num for  num in range(N+1)]

edges = []

for i in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
answer = 0

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += cost

print(answer)


