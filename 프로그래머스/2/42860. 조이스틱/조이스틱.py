def solution(name):
    answer = 0
    n = len(name)
    ord_A = ord('A')
    ord_Z = ord('Z')
    # 1. 각 문자마다 몇 번 이동이
    for text in name:
        # 위로 조작이 빠름
        ord_text = ord(text)
        
        if ord_text - ord_A  <= 12:
            answer += ord_text - ord_A
        #아래로 조작이 빠름
        else:
            answer += ord_Z - ord_text + 1 # A에서 부터 가니까!
    
    # 2. 문자 간 이동 횟수
    move = n - 1
    for i in range(n):
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
        move = min(move, i*2 + (n-j), (n-j)*2 + i)
    answer += move
    return answer