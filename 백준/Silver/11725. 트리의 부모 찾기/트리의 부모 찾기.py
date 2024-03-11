N = int(input()) # 노드의 개수 N 입력

# 트리 생성 
# 각 노드에 대해서 빈 리스트로 생성
tree = [[] for _ in range(N+1)]

# N-1번만큼 반복
for _ in range(N-1):
    A, B = map(int, input().split()) # 두 정점 입력받기
    tree[A].append(B) # 각 노드에 정점 추가
    tree[B].append(A) # 각 노드에 정점 추가
    
parents = [0] * (N+1) # 부모 노드 저장할 공간 - 0으로 초기화 - 1부터 시작
stack = [(1, 0)] # 루트 node와 부모 노드 전달(임의로 루트 노드의 부모 노드는 0이라고 설정)

# stack에 값이 있으면 계속 반복
while stack:
    node, parent = stack.pop() # stack의 있는 값을 node와 parent에 저장
    parents[node] = parent # parents라는 공간에 부모 노드들을 저장
    for child in tree[node]: # 각 노드들의 자식 node 들을 탐색
        if parents[child] == 0: # 만약에 해당 node의 parent 노드가 parents에 저장 되어있지 않다면 
            stack.append((child, node)) # stack에 해당 node와 부모 노드를 저장

# 부모 노드만 출력
for i in range(2, N+1): # 2번 노드부터 출력
    print(parents[i])