answer = 0

def dfs(total, step, n, numbers, target):
    global answer
    if n == step:
        if total == target:
            answer += 1
            return
        else:
            return 

    dfs(total+numbers[step], step+1, n, numbers, target)
    dfs(total-numbers[step], step+1, n, numbers, target)

def solution(numbers, target):
    global answer
    n = len(numbers)
    dfs(0, 0, n, numbers, target)
    
    return answer