from collections import defaultdict, deque

def solution(n, wires):
    answer = 100
    hash_wires = defaultdict(list)
    
    for wire in wires:
        one, two = wire
        hash_wires[one].append(two)
        hash_wires[two].append(one)
    
    for wire in wires:
        one, two = wire
        visited = [False] * (n+1)
        q = deque()
        q.append(one)
        visited[one] = True
        visited[two] = True
        count_one = 1
        
        while q:
            now = q.popleft()
            for node in hash_wires[now]:
                if not visited[node]:
                    visited[node] = True
                    q.append(node)
                    count_one += 1
        count_two = n - count_one  
        answer = min(abs(count_two-count_one), answer)
        
    
    
    return answer