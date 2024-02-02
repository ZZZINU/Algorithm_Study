# 2961번: 도영이가 만든 맛있는 음식 (⚪실버_2)
from itertools import combinations # 조합을 사용하기 위해 라이브러리 사용

N = int(input()) # 재료의 개수 N 입력

S_list = [] # 신맛 저장
B_list = [] # 쓴맛 저장

# 신맛과 쓴맛 입력 -> 리스트에 저장
for i in range(N):
    S, B = map(int, input().split())
    S_list.append(S)
    B_list.append(B)

S_combi_product = [] # 신맛 조합의 곱셈 결과 모두 저장
B_combi_sum = [] # 쓴맛 조합의 덧셈 결과 모두 저장

# 재료를 사용하여 신맛 조합 구하기 -> 1부터 N개의 구성 요소로 이루어진 조합
for i in range(1, N + 1):
    S_combi = list(combinations(S_list, i)) # i개의 요소로 이루어진 모든 조합 추출
    for combi in S_combi: # 각 조합에 대해서 반복
        product = 1 # 곱셈의 결과값 저장
        for num in combi: # 각 조합의 각 요소에 대해서 반복
            product *= num # 각 요소들을 모두 곱해서 product에 저장
        S_combi_product.append(product) # 모두 곱한 결과값을 S_combi_product에 저장
        
# 재료를 사용하여 쓴맛 조합 구하기 -> 1부터 N개의 구성 요소로 이루어진 조합
for i in range(1, N + 1):
    B_combi = list(combinations(B_list, i)) # i개의 요소로 이루어진 모든 조합 추출
    for combi in B_combi: # 각 조합에 대해서 반복
        total = 0 # 덧셈의 결과값 저장
        for num in combi: # 각 조합의 각 요소에 대해서 반복
            total += num # 각 요소들을 모두 더해서 total에 저장
        B_combi_sum.append(total) # 모두 더한 결과값을 B_combi_sum에 저장

diff = [] # 신맛과 쓴맛의 차이를 저장

# 각 조합의 결과에 대해서 신맛과 쓴맛의 차이를 모두 저장
for i in range(len(S_combi_product)):
    diff.append(abs(S_combi_product[i]-B_combi_sum[i])) # abs(): 절댓값 반환

print(min(diff)) # 신맛과 쓴맛의 차이가 가장 작은 요리의 차이 출력
    
