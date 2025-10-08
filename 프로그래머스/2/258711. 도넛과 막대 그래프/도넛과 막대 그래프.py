from collections import defaultdict

def solution(edges):
    indeg = defaultdict(int) # 기본값 0: indeg[v]는 v로 들어오는 간선 수
    outdeg = defaultdict(int) # 기본값 0: outdeg[v]는 v에서 나가는 간선 수
    nodes = set() # 그래프에 등장하는 모든 정점 모음
    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1
        nodes.add(a)
        nodes.add(b)
        
    # 1. 정점 찾기
    generated = None
    for v in nodes:
        if indeg[v] == 0 and outdeg[v] >= 2:
            generated = v
            break
            
    # 2. 정점과 연결된 간선의 개수 세기 = 모양 그래프의 총개수
    total_graphs = outdeg[generated]
    
    # 3. 생성된 정점과 연결된 간선을 모두 삭제
    indeg2 = dict(indeg)
    outdeg2 = dict(outdeg)
    
    outdeg2[generated] = 0
    
    for a, b in edges:
        if a == generated:
            indeg2[b] -= 1
    
    # 4. 모양 갯수 세기
    stick = 0 
    eight = 0
    
    for v in nodes:
        if v == generated:
            continue
        
        # 막대: in-degree == 0 인 정점의 개수 = 막대 그래프 개수
        if indeg2.get(v, 0) == 0:
            stick += 1
        
        # 8자: in=2 & out=2
        if indeg2.get(v, 0) == 2 and outdeg2.get(v, 0) == 2:
            eight += 1
    
    donut = total_graphs - stick - eight
    
            
        
    return [generated, donut, stick, eight]