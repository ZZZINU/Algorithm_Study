class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, nums):
        cur = self.root
        for num in nums:
            if num not in cur:
                cur[num] = {}
            cur = cur[num]
            
            if 0 in cur:
                return False
        
        if cur:  # 트라이 끝에 다른 숫자가 추가되어 있는지 확인
            return False
        
        cur[0] = True  # 전화번호의 끝을 표시
        return True
        
import sys
input = sys.stdin.readline

t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    trie = Trie()
    consistent = True

    phone_numbers = [input().strip() for _ in range(n)]
    phone_numbers.sort()  # 짧은 길이 순서대로 정렬 (접두사 여부 쉽게 검사 가능)

    for data in phone_numbers:
        if not trie.insert(data):
            consistent = False
            break
        
    if consistent:
        print("YES")
    else:
        print("NO")
