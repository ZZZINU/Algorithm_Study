from collections import deque
    
def solution(board, moves):
    answer = 0
    n = len(board)
    new_board = [deque() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                new_board[j].append(board[i][j])
            
    basket = []
    count = 0
    
    for move in moves:
        if new_board[move-1]:
            doll = new_board[move-1].popleft()
            if basket and basket[-1] == doll:
                basket.pop()
                count += 1
            else:
                basket.append(doll)
        


    return count * 2
