answer = 0
def DFS(numbers, target, step, value):
    global answer
    if len(numbers) == step and target == value:
        answer+=1
        return
    
    if len(numbers) == step:
        return 
        
    
    DFS(numbers, target, step+1, value + numbers[step])
    DFS(numbers, target, step+1, value - numbers[step])

def solution(numbers, target):
    global answer
    DFS(numbers, target, 0, 0)
    
    return answer