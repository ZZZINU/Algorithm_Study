# 2800번: 괄호 제거
from itertools import combinations

expression = list(input())

bracket_left = []
bracket_index = []

result = set()

for i in range(len(expression)):
    if (expression[i] == '('):
        bracket_left.append(i)
    elif (expression[i] == ')'):
        bracket_index.append((bracket_left.pop(), i))

for i in range(1, len(bracket_index)+1):
    combi = list(combinations(bracket_index, i))

    for c in combi:
        temp = expression[:]
        for x, y in c:
            temp[x] = ''
            temp[y] = ''
        result.add(''.join(temp))

result = list(result)
result.sort()

for item in result:
    print(item)
