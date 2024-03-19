# 2960번: 에러토스테네스의 체 (⚪실버_4)

N, K = map(int, input().split()) # N, K 입력

order = 0 # 지워진 순서 체크

# 2부터 N까지 모든 정수 저장
my_list = [] 
for i in range(2,N+1):
    my_list.append(i)

# K번째 지워진 수를 찾을 때까지 반복
while order != K:
    P = min(my_list) # P: 아직 지우지 않은 수 중 가장 작은 수
    temp = [] # 아직 지우지 않은 수 임시 저장
    
    # my_list에 있는 원소 전부 다 체크
    for num in my_list:
        if num % P == 0 : # 아직 지우지 않은 P의 배수라면
            order += 1 # 지워진 순서 +1 증가 -> 그 num을 지우는 것 
        else: # P의 배수가 아니라면
            temp.append(num) # temp에 추가
        
        if order == K: # K번째 지워진 수에 도달했다면
            break # 반복 중지
    
    #  K번째 지워진 수에 아직 도달하지 못했다면
    my_list = temp # 지우지 않은 수들을 다시 my_list에 저장

print(num) # K번째 지워진 수 출력