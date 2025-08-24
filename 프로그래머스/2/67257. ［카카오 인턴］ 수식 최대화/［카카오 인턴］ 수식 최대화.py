from itertools import permutations
import re

def solution(expression):
    answer = 0
    
    operation_list = list()
    if '*' in expression:
        operation_list.append('*')
    if '+' in expression:
        operation_list.append('+')
    if '-' in expression:
        operation_list.append('-')
        
    operation_permutations = list(permutations(operation_list))
    expression = re.split('([^0-9])', expression)
    print(expression)
    
    for operation_permutation in operation_permutations:
        copied_expression = expression[:]
        for operator in operation_permutation:
            while operator in copied_expression:
                op_idx = copied_expression.index(operator)
                
                cal = str(eval(copied_expression[op_idx-1] + copied_expression[op_idx] + copied_expression[op_idx+1]))
                
                # 연산자와 앞 뒤의 숫자를 없애고 결괏값을 배열에 넣기
                copied_expression[op_idx-1] = cal
                copied_expression = copied_expression[:op_idx] + copied_expression[op_idx+2:]
        
        answer = max(answer, abs(int(copied_expression[0])))
                
            
    
    return answer