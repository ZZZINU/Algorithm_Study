# 5557번: 1학년 (🟡골드_5)
N = int(input()) # 숫자의 개수 N 입력
nums = list(map(int, input().split())) # 정수 N개 입력

# dp: 현재까지의 수가 나올 수 있는 경우의 수 저장
# dp[인덱스][현재까지의 수] = 가능한 경우의 수
# N-1개의 행 
# 21개의 열
dp = [[0]*21 for _ in range(N-1)] 

# 첫 번째 숫자를 만들 수 있는 경우의 수는 1개
dp[0][nums[0]] = 1

# 두 번째 숫자부터 마지막에서 두 번째 숫자까지 반복
for i in range(1, N-1):
    for j in range(21): # 0~20까지 반복
        # 중간에 나오는 수가 모두 0 이상 20 이하
        if j-nums[i]>=0: # 0과 20 사이의 값 j에서 현재의 수 (nums[i])를 뺐을 때 0 이상이라면
            dp[i][j-nums[i]] += dp[i-1][j] # 이전 dp의 j를 만들 수 있는 경우의 수를 더한다 
        if j+nums[i]<=20: # 0과 20 사이의 값 j에서 현재의 수 (nums[i])를 더했을 때 20 이하라면 
            dp[i][j+nums[i]] += dp[i-1][j] # 이전 dp의 j를 만들 수 있는 경우의 수를 더한다 

print(dp[-1][nums[-1]]) # dp의 마지막 행에서 nums의 마지막 숫자를 만들 수 있는 경우의 수 출력
