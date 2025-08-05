def solution(string):
    stack = []
    for text in string:
        if text == "(":
            stack.append(text)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True