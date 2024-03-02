# 11403번: 경로 찾기 (⚪실버_1)
from collections import deque
N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))


def bfs(start):
    visited = [False] * N
    queue = deque([start])

    while queue:
        current_node = queue.popleft()
        for next_node in range(N):
            if graph[current_node][next_node] == 1 and not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

    return visited


answer = []

for i in range(N):
    answer.append(bfs(i))

for row in answer:
    for val in row:
        if val == True:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()