# 1405번: 미친 로봇

def back_tracking(x, y, percent, count):
    global result

    # 만약에 N번만큼 돌았으면 종료!
    if count == num:
        result += percent # 지금까지 축적된 확률
        return
    
    plane[x][y] = 1 # 방문 표시

    # 동서남북 움직이기
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        
        if plane[new_x][new_y] == 1: # 이미 방문했던 곳이라면
            continue # 패스
        else: # 방문 안 한 경우라면
            back_tracking(new_x, new_y, percent * dir_percent[i], count+1) # 확률, 횟수 반영해서 재귀로 함수 돌리기
            plane[new_x][new_y] = 0 # 상태 복원

# 해결 방법
# 단순한 경로만 확률에 더하자!

num, E, W, S, N = map(int, input().split()) # 입력

dir_percent = [E/100, W/100, S/100, N/100] # 퍼센트로 바꾸기

dx = [0, 0, -1, 1] # x좌표 이동
dy = [-1, 1, 0, 0] # y좌표 이동

plane = [[0]*(num*2+1) for _ in range(num*2+1)] # 평면 0으로 초기화 -> 1은 방문한 곳!

result = 0 # 로봇의 이동 경로가 단순할 확률

# x좌표, y좌표, 확률 (최초니까 1로 설정), 횟수 
# x, y 초기 좌표가 num인 이유 : 중간지점
back_tracking(num, num, 1, 0)

# 출력
print(result)
