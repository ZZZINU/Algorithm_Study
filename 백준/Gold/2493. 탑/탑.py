N = int(input()) # 탑의 수 입력

top = list(map(int, input().split())) # 탑들의 높이 입력

result = [] # 레이저 신호 수신 탑들의 번호 저장
stack = [] # stack

# 탑의 수만큼 반복
for i in range(N):

    while stack: # stack에 값이 있다면
        if stack[-1][1] > top[i]: # 탑 높이 비교 => 수신 가능한 상황 
            result.append(stack[-1][0] + 1) # 수신한 탑의 (인덱스 + 1) 번호 추가
            break # 수신 완료 => while문 중단 
    
        else: # 수신이 불가능 하다면
            stack.pop() # stack에 있는 값 pop()
        
    if not stack: # stack에 값이 없다면 == 레이저를 수신할 탑이 없음
        result.append(0) # 따라서 0을 추가
    
    stack.append([i, top[i]]) # stack에 인덱스와 탑의 높이를 추가
    
# 레이저 신호를 수신한 탑들의 번호를 출력
print(" ".join(map(str, result)))