# 9934번: 완전 이진 트리(⚪실버_1)

def find_root(buildings, result):
    new_buildings = []
    
    for i in range(len(buildings)):
        root_index =  (len(buildings[i]) - 1) // 2
        result.append(buildings[i][root_index])
        
        left_part = buildings[i][:root_index]
        right_part = buildings[i][root_index+1:]
        
        new_buildings.append(left_part)        
        new_buildings.append(right_part)
    
    return new_buildings

K = int(input())
buildings = [list(map(int, input().split()))]

buildings_len = pow(2, K) - 1
result = []

while len(buildings[0]) != 0:
    buildings = find_root(buildings, result)

for i in range(K):
    print(' '.join(map(str, result[pow(2, i)-1:pow(2,i+1)-1])))
