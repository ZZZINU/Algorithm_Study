def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[i] > numbers[stack[-1]]:
            index = stack.pop()
            answer[index] = numbers[i]
        stack.append(i)
    return answer