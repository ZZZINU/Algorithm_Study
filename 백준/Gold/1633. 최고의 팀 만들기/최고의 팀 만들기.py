# 1633번: 최고의 팀 만들기
dp = [[0] * 16 for _ in range(16)]

while True:
    try:
        white, black = map(int, input().split())
        
        for w in range(15, -1, -1):
            for b in range(15, -1, -1):
                if w != 0:
                    # 백 선수 영입 X | 백 선수 영입 O
                    dp[w][b] = max(dp[w][b], dp[w-1][b] + white)
                if b != 0:
                    # 흑 선수 영입 X | 흑 선수 영입 O
                    dp[w][b] = max(dp[w][b], dp[w][b-1] + black)

    except:
        print(dp[15][15])
        break




