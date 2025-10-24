from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    check = [-1 for _ in range(n+1)]
    print(check)
    check[1] = 0 
    # print(graph)
    
    for vertex in edge:
        a, b = vertex
        graph[a].append(b)
        graph[b].append(a)
    # print(graph
    q = deque()
    q.append((1, 0))
    max_num = 0
    
    while q:
        node, step = q.popleft()
        max_num = step
        # print(node, step)
        for v in graph[node]:
            if check[v] == -1:
                check[v] = step + 1
                q.append((v, step + 1))


    return check.count(max_num)