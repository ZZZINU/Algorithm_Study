
def solution(d, budget):
    answer = 0
    my_budget = budget
    d.sort()
    
    for need in d:
        if my_budget >= need:
            answer += 1
            my_budget -= need
        else:
            break
    
    return answer