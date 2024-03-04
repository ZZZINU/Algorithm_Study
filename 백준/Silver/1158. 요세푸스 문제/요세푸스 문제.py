from sys import stdin

my_dict = {} # 빈 리스트 생성
N, K = map(int, stdin.readline().split()) # N, K 입력 받기

for i in range(1, N+1):
    my_dict[i] = 0

point = 0
order = 1;

while True:
    
    if all(value>0 for value in my_dict.values()):
        break
    
    for i in my_dict:
        if my_dict[i] == 0:
            point += 1
            if point == K:
                point = 0
                my_dict[i] = order
                order += 1

my_result = sorted(my_dict.items(), key=lambda x: x[1])


print("<", end="")
print(", ".join(map(str, [pair[0] for pair in my_result])), end="")
print(">", end="")
