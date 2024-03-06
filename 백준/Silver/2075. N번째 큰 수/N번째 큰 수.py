from sys import stdin

N = int(stdin.readline())
table = []

if 1 <= N <= 1500:
    for i in range(N):
        row = set(map(int, input().split()))

        if all(-1000000000 <= value <= 1000000000 for value in row):
            table.extend(row)
            table.sort()
            table = table[-(i+1):]

        else:
            print("표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이어야 합니다.")
            
    print(table[-N])
else:
    print("N은 1이상 1500이하의 값이어야 합니다.")