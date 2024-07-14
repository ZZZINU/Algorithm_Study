# 7453번: 합이 0인 네 정수
import sys
input = sys.stdin.readline

A_list = []
B_list = []
C_list = []
D_list = []

# 입력
n = int(input())
for i in range(n):
    A, B, C, D = map(int, input().split())
    A_list.append(A)
    B_list.append(B)
    C_list.append(C)
    D_list.append(D)


dic = {} # 딕셔너리 사용!
count = 0 # 합이 0이 되는 쌍의 개수 저장

# A와 B의 합을 딕셔너리에 저장
for a in A_list:
    for b in B_list:
        AB = a+b
        if AB in dic:
            dic[AB] += 1 # 합이 이미 저장된 값이라면 +1
        else:
            dic[AB] = 1 # 합이 새로운 값이라면 =1

# C와 D의 합의 음수가 딕셔너리에 있는지 확인하고, 있으면 그 값을 count에 더하기
for c in C_list:
    for d in D_list:
        # A+B+C+D 합이 0이어야 하니까 CD의 합은 음수겠지! 
        # dic에는 양수로 저장되어있으니까 -1 곱해주는 것
        CD = (c+d) * -1 
        if CD in dic:
            count += dic[CD] 

# 출력
print(count)