count = [] # 각 테스트 케이스에 대한 중앙값의 개수
result = [] # 각 테스트 케이스에 대한 중앙값들

T = int(input()) # 테스트 케이스의 개수

# 테스트 케이스의 개수만큼 반복
for i in range(T):
    
    M = int(input()) # 수열의 크기
    temp = [] # 각 중앙값 계산하기 위한 temp
    sequence = [] # 수열
    
    # 중앙값의 개수 계산 (짝/홀 나눠서)
    if M%2 == 0:
        count.append(int(M/2))
    else:
        count.append(int((M+1)/2))

    # 중앙값 계산
    while True:
        
        # 입력한 원소의 개수가 입력한 수열의 크기(M)과 같다면 while문 빠져나오기 (입력 중지)
        if len(sequence) == M:
            for i in range(M): # 수열의 크기만큼 반복 
                temp.append(sequence[i]) # 수열에서 하나씩 뽑아서 temp에 저장
                
                if i % 2 == 0: # 홀수번째 수라면  
                    temp.sort() # temp 오름차순 정렬
                    result.append(temp[int((i+1)/2)]) # result에 계산한 중앙값 저장           
            break
        
        elements = map(int, input().split()) # 수열의 원소들 입력 (10개씩)
        sequence.extend(elements) # 수열에 저장

start = 0 # 각 테스트 케이스의 시작 인덱스

# 출력
# 테스트 케이스 개수만큼 반복
for i in range(T):
    
    if i != 0: # 가장 처음 (인덱스 0) 이 아닌 경우에는 해당 테스트 케이스의 인덱스 계산 
        start += count[i-1]
    
    print(count[i]) # 중앙값의 개수 출력
    
    step = result[start:start + count[i]] # 해당 테스트 케이스의 중앙값들만 뽑아내기
    
    # 한 줄에 10개씩 출력
    for j in range(0, len(step), 10):
        print(' '.join(str(num) for num in step[j:j+10]))

