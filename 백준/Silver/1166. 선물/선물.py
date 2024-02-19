#1166번: 선물

# N, L, W, H 입력
N, L, W, H = map(int, input().split())

# 한 변의 최대 길이
# 직육면체 각 변의 길이 또는 부피의 세제곱근 보다는 작아야 함.
max = min(L, W, H, (L*W*H / N)**(1/3))
min_len = 0 
mid = 0

# 만약에 N이 1이면 직육면체 가로, 세로, 높이 중에서 가장 작은 값으로 설정
if N == 1:
    print(min(L, W, H))
else:
    # min 이 max를 넘을 때까지 반복
    while min_len <= max:

        # max와 min의 중간값을 구한다
        temp = mid
        mid = (min_len+max)/2
        
        # 이전과 같이 똑같은 경우에는 반복문을 종료
        # 콘솔창에 출력되지 않는 미미한 차이는 무시
        if temp == mid:
            break
        
        # 중간값으로 넣을 수 있는 박스의 개수 구하기
        count = (L // mid) * (W // mid) * (H // mid )
        
        # 넣을 수 있는 박스의 개수가 N보다 작으면 한 변의 길이를 줄이기
        if count < N:
            max = mid
        # 아니라면 한 변의 길이를 늘리기
        else:
            min_len = mid
    
    # 최대 한 변의 길이 출력
    print(max)