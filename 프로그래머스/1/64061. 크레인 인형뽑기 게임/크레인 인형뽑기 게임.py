def solution(board, moves):
    answer = 0
    basket = []
    new_board = [[] for _ in range(len(board[0]))]

    # board를 회전하여 new_board로 변환
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                new_board[j].append(board[i][j])

    # moves를 처리
    for move in moves:
        # move는 1-based index이므로 0-based로 변환
        column = move - 1
        if new_board[column]:  # 해당 열에 인형이 남아 있는 경우
            doll = new_board[column].pop()  # 인형을 뽑음
            # basket의 마지막 인형과 비교
            if basket and basket[-1] == doll:
                basket.pop()  # 동일하면 제거
                answer += 2  # 인형 2개 제거
            else:
                basket.append(doll)  # 그렇지 않으면 추가

    return answer
