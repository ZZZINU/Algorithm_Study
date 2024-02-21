from itertools import combinations # 조합 - 라이브러리 사용
 
N, S = map(int, input().split()) # 정수의 개수를 나타내는 N과 정수 S 입력
nums = list(map(int, input().split())) # 수열 입력

count = 0 # 합이 S가 되는 부분 수열의 개수 저장

# 원소가 1~N개까지인 조합을 구하기
for i in range(1, N+1):
    result = combinations(nums, i)
    
    # 각 조합의 원소의 합이 S라면 count +1 증가
    for num in result:
        if sum(num) == S:
            count += 1

#  합이 S가 되는 부분수열의 개수 출력
print(count)