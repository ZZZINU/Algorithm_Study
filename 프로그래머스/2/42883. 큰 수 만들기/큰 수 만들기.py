def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
            
        stack.append(num)
    # print(stack)
    if k > 0:
        stack = stack[:-k]
    # print(stack)
        
    return "".join(stack)