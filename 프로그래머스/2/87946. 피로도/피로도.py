from itertools import permutations

def solution(hp_origin, dungeons):
    answer = -1
    for i in range(len(dungeons), 0, -1):
        case = list(permutations(dungeons, i))
        for j in range(len(case)):
            hp = hp_origin
            for k in range(i):
                temp = case[j][k]
                if hp >= case[j][k][0]:
                    hp -= case[j][k][1]
                    if k == i-1:
                        answer = i
                else:
                    break
            if answer != -1: 
                break
        if answer != -1: 
            break

    return answer