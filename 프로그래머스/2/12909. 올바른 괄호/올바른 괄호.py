def solution(s):
    answer = True
    stack = []
    
    for item in s:
        if item == '(':
            stack.append('(')
        elif item == ')' and stack:
            stack.pop()
        else:
            return False
    
    if stack:
        return False

    return True