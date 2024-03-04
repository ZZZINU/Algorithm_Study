operand = [] # 피연산자
num = [] # 알파벳에 해당하는 값

N = int(input()) # 피연산자의 개수
postfix = input() # 후위 표기식

# 알파벳에 해당하는 값 입력
for i in range (N):
    num.append(input())

# 후위 표기식의 길이만큼 반복
for i in list(postfix):
    
    # 피연산자를 만난 경우
    if 'A' <= i <= 'Z':
        # 알파벳을 대신할 숫자를 num에서 가져와서 operand에 넣기
        operand.append(num[ord(i)-ord('A')]) 

    # 연산자를 만난 경우
    elif i == '+':
        a = float(operand.pop())
        b = float(operand.pop())
        operand.append(a+b)
    elif i == '-':
        a = float(operand.pop())
        b = float(operand.pop())
        operand.append(b-a)
    elif i == '*':
        a = float(operand.pop())
        b = float(operand.pop())
        operand.append(a*b)
    elif i == '/':
        a = float(operand.pop())
        b = float(operand.pop())
        operand.append(b/a)
    else:
        print("예외") 
        
# 소숫점 둘째짜리까지 출력
print("{:.2f}".format(operand.pop()))  

