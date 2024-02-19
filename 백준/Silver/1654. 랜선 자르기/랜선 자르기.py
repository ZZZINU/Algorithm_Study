#1654번: 랜선 자르기 (⚪실버_3)

# N: 필요한 랜선의 개수
# K: 이미 가지고 있는 랜선의 개수
# 입력
K, N = map(int, input().split())

total = 0 # 랜선의 총 길이를 저장
cable = []

# 각 랜선의 길이 입력
for i in range(K):
    temp = int(input())
    cable.append(temp)
    total += temp

max = total // N + 1 # 각 랜선의 최대 길이
min = 1 # 각 랜선의 최소 길이

# min이 max를 넘어갈 때까지 반복
while min <= max:
    mid = (max+min)//2 # min과 max의 중간값
    count = 0 # 만들 수 있는 랜선의 개수

    # 각 랜선에 대해서 만들 수 있는 랜선의 개수 구하기
    for length in cable:
        count += length // mid
    
    # (만들 수 있는 랜선의 개수 >= 필요한 랜선의 개수)인 경우
    #  하나의 랜선의 길이를 늘리자
    if count >= N:
        min = mid + 1
    # 아니면 하나의 랜선의 길이를 줄이자
    else:
        max = mid - 1
    
# 랜선의 최대 길이 출력
print(max)

