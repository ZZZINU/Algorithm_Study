

from collections import deque


# 쌍이 맞다 -> 균형잡힌 괄호 문자열
# 짝도 맞다 -> 올바른 괄호 문자열

def is_correct_parentheses(string):
    # 올바른 괄호 문자열인지 체크
    stack = []
    for text in string:
        if text == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True

def separate_to_u_v(string):
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char

        if char == "(":
            left += 1
        else:
            right += 1

        if left == right:
            break

    v = ''.join(list(queue))
    return u, v

# 괄호 뒤집는 함수
def reverse_parentheses(string):
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string

def change_to_correct_parentheses(string):
    if string == '':
        return ''

    u, v = separate_to_u_v(string)
    if is_correct_parentheses(u):
        return u + change_to_correct_parentheses(v)
    else:
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)

def solution(p):
    
    answer = get_correct_parentheses(p)
    return answer



    
