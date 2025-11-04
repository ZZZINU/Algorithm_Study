def solution(arr):
    n = len(arr)
    zero, one = 0, 0
    
    def compress(r, c, size):
        nonlocal zero, one
        first = arr[r][c]
        same = True
        
        for i in range(r, r + size):
            if not same:
                break
            for j in range(c, c + size):
                if arr[i][j] != first:
                    same = False
                    break
        if same:
            if first == 0:
                zero += 1
            else:
                one += 1
            return
        
        half = size // 2
        compress(r, c, half)
        compress(r, c + half, half)
        compress(r + half, c, half)
        compress(r + half, c + half, half)
    
    compress(0, 0, n)
    
    return [zero, one]