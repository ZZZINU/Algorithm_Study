def solution(n):
    answer = 0
    def dfs(board, row, n):
        count = 0
        if row == n:
            return 1
        
        for col in range(n):
            board[row] = col # row 행에 c 열에 퀸이 있음
            
            for i in range(row):
                # 같은 열에 있나?
                if board[i] == board[row]:
                    break
                # 대각선에 있나?
                if abs(board[i]-board[row]) == row - i:
                    break
            else:
                count += dfs(board, row+1, n)
                
        return count
                    
    answer = dfs([0]*n, 0, n)
    return answer