# 17266번: 어두운 굴다리 (⚪실버_4)

N = int(input()) # 굴다리의 길이 N 입력
M = int(input()) # 가로등의 개수 M 입력
x = list(map(int, input().split())) # 가로등의 위치 입력

max_length = 0 # 가로등 사이의 최대 길이를 저장
for i in range(1, M): # M만큼 반복
    # 가로등 사이의 최대 길이를 계속해서 갱신
    max_length = max(x[i]-x[i-1], max_length) 

# 최종적인 높이는 
# 1) 가로등 사이의 최대 길이를 2로 나눈 값 (2개의 가로등 사이를 비추면 되니까)
# 2) 시작 지점부터 첫번째 가로등까지의 거리
# 3) 마지막 지점부터 마지막 가로등까지의 거리
# 중에서 가장 큰 값으로 설정하면 된다!
height = max((max_length+1)//2, x[0]-0, N-x[-1])

print(height) # 굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이 출력