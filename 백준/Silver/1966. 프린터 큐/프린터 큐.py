from collections import deque # deque 사용

result = [] # 결과 저장할 리스트
count = int(input()) # 총 반복 횟수 (프린트 횟수)

for i in range(count):
    order = 0 # 인쇄 순서
    N, M = map(int, input().split()) # 문서의 개수: N, 몇 번째로 인쇄되었는지 궁금한 문서: M
    
    queue = deque(map(int, input().split())) # 문서의 중요도
    
    # 인쇄 순서 구할 때까지 반복
    while True:
        
        # 가장 높은 중요도, 현재 Queue의 가장 앞에 있는 문서의 중요도 저장
        if N == 1: 
            temp_max = queue[0]
        else:
            temp_max = max(queue)
        temp = queue.popleft()
        
        # M의 인덱스가 0인 경우
        if M == 0:
            if temp == temp_max: # 가장 높은 중요도라면 출력 
                order += 1 # 인쇄 순서 +1 증가 
                result.append(order) # result에 인쇄 순서를 저장
                break 
            else: # 가장 높은 순서가 아니라면
                M = len(queue) # M의 인덱스를 가장 마지막으로 변경
                queue.append(temp) # Queue의 가장 뒤에 재배치
            
        # 현재 Queue의 가장 앞에 있는 문서의 중요도가 가장 높은 중요도인 경우
        elif temp == temp_max:
            M -= 1 # M의 인덱스를 하나 감소
            order += 1 # 인쇄 순서 +1 증가 

        # 현재 Queue의 가장 앞에 있는 문서의 중요도가 가장 높은 중요도가 아닌 경우
        else:
            queue.append(temp) # Queue의 가장 뒤에 재배치
            M -= 1 # M의 인덱스를 하나 감소
            

# 결과 출력
for i in range(count):
    print(result[i])



