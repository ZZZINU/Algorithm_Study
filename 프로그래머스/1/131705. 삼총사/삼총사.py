import itertools

def solution(number):
    answer = 0
    combi = list(itertools.combinations(number, 3))
    for item in combi:
        if sum(item) == 0:
            answer += 1
            

    return answer