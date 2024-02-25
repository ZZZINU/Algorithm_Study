# 1764번: 듣보잡 (⚪실버_4)

# 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M 입력
N, M = map(int, input().split())

names = set() # 이름 저장
result = [] # 듣도 못한 사람의 명단

# 듣도 못한 사람의 이름 저장
for _ in range(N):
    names.add(input())

# 보도 못한 사람의 이름 입력과 동시에
# 듣도 못한 사람이었는지 검사
# 중복되는 이름이라면 result에 저장 
for _ in range(M):
    temp = input()
    if temp in names:
        result.append(temp)

result.sort() # 이름을 사전순으로 정렬ㄴ

print(len(result)) # 듣보잡의 수 출력

for item in result: # 듣보잡의 명단 출력
    print(item)
