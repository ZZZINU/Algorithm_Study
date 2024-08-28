total = int(input())
count = int(input())
result = 0 

num1 = []
num2 = []
for i in range(0, count):
    a, b = map(int, input().split())
    num1.insert(i, a)
    num2.insert(i, b)


for i in range(0, count):
    result += num1[i] * num2[i]

if total == result:
    print("Yes")
else:
    print("No") 