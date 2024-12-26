def solution(park, routes):
    park_map = [list(row) for row in park] # 문자열을 리스트로 변환
    park_width = len(park[0])
    park_height = len(park)
    

    # 시작 위치 찾기
    for i in range(park_height):
        if 'S' in park[i]:
            x, y = i, park[i].index('S')
            break
    print(x, y)
    
    # 방향별 이동 값
    directions = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    
    # 경로 따라 이동
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        dx, dy = directions[direction]
        
        # 이동 가능한지 확인
        can_move = True
        for step in range(1, distance + 1):
            nx, ny = x + dx * step, y + dy * step
            
            # 경계 확인 및 장애물 확인
            if not (0<= nx <park_height and 0<= ny < park_width) or park_map[nx][ny] == 'X':
                can_move = False
                break
        
        if can_move:
            x += dx * distance
            y += dy * distance
        
    


    return (x, y)