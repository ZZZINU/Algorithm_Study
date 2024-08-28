# 14725번: 개미굴 
class Trie:

    # 루트 노트 초기화
    def __init__(self): 
        self.root = {} # 빈 딕셔너리로 초기화

    # 먹이를 리스트에 추가
    def add(self, foods):
        cur = self.root # 현재 위치 

        for food in foods:
            if food not in cur:
                # 현재 노드에 food가 없으면 자식 노드 추가
                cur[food] = {}
            # 현재 위치를 자식 노드로 이동
            cur = cur[food]
        cur[0] = True # 리프 노드 표시
    
    # DFS
    def travel(self, level, cur):

        # 현재 노드에 0이 있으면, 해당 노드는 리프 노드
        # -> 더 이상 탐색 X
        if 0 in cur:
            return
        
        # 현재 노드의 자식 노드들을 정렬
        cur_child = sorted(cur)

        # 자식 노드들을 순차적으로 탐색
        for ch in cur_child:
            print("--" * level + ch)
            self.travel(level+1, cur[ch])

N = int(input())

trie = Trie()

for i in range(N):
    data = list(input().split())
    trie.add(data[1:])

trie.travel(0, trie.root)

