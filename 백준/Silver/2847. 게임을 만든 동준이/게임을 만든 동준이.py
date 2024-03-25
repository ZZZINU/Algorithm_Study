# 2847번: 게임을 만든 동준이(⚪실버_4)

N = int(input()) # 레벨의 수 N 입력
point = [] # 각 레벨을 클리어하면 얻는 점수들 저장
reduction = 0 # 몇 번 감소시키면 되는지 저장 

# 각 레벨을 클리어하면 얻는 점수 입력
for _ in range(N):
    temp = int(input()) # 점수 입력
    point.append(temp) # point에 저장

# point에 점수가 2개 이상 있을 때까지만 반복
while len(point) > 1:
    next_level = point.pop() # point에서 마지막 레벨 점수 추출
    prev_level = point.pop() # point에서 마지막 레벨에서 하나 전 레벨 점수 추출

    while next_level <= prev_level: # 다음 레벨 점수보다 이전 레벨 점수가 크다면 
        prev_level -= 1 # 이전 레벨 점수 -1 감소
        reduction += 1 # 감소 횟수 +1 증가
    
    point.append(prev_level) # point 리스트에 prev_level의 감소된 점수 추가

print(reduction) # 점수를 몇 번 감소시키면 되는지 출력