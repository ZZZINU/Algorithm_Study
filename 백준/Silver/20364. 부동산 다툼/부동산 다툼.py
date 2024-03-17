# 20364번: 부동산 다툼

duck = []
result = []
N, Q = map(int, input().split())
for i in range(1, Q+1):
    duck.append(int(input()))
    
tree = [[] for _ in range(N+1)]

for i in range(Q):
    num = duck[i]
    check = []
    
    while num != 1:
        check.append(num)
        num = num // 2 
    check.append(1)
    
    for j in range(len(check)):
        check_num = check.pop()
        if 1 in tree[check_num]:
            result.append(check_num)
            break
        
    else:
        tree[duck[i]].append(1)
        result.append(0)
            
        
for item in result:
    print(item)