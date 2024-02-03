# 14501번: 퇴사 (⚪실버_3)

N = int(input()) # N일 입력 
schedule_list = [] # 상담 일정표 저장

# 상담 일정표 입력
for i in range(N):
    temp = list(map(int, input().split()))
    schedule_list.append(temp)

# dp : 각 날짜까지의 최대 이익을 저장
# 왜 N+1? 
# -> 상담 일정의 마지막 날 다음 날을 포함하여 계산
# -> 그래야 상담이 끝난 다음 날에 대한 최대 이익을 계산할 수 있어서
dp = [0 for i in range(N+1)]

# 모든 상담에 대한 최대 이익을 계산
# i번째까지 일했을 때 얻는 최대 수익
for i in range(N):
    # i번째 날에 상담을 진행했을 때, [상담이 가능한 모든 날짜] 에 대해서 반복
    # 즉, ((i+상담 기간 ~ 마지막날))
    for j in range(i+schedule_list[i][0], N+1):
        # j를 기준으로 상담했을 때 얻는 최대 수익을 dp에 저장
        # 만약 j번째에서의 최대 이익이 i번째에서 상담을 끝낸 후의 이익보다 작다면 업데이터
        if dp[j] < dp[i] + schedule_list[i][1]:
            dp[j] = dp[i] + schedule_list[i][1]
    
# 얻을 수 있는 최대 이익 출력
print(dp[-1])
