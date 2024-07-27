# 3107번: IPv6
address = list(input().split(":"))

result = []
check = True

count = 0 
for item in address:
    if item != "":
        count += 1

for item in address:
    if item == '' and check:
        for i in range(8-count):
            result.append("0000")
            check = False
    else:
        if item != '':
            result.append(item)
    

for index, item in enumerate(result):
    if index == 7:
        print(item.rjust(4, '0'))
        exit()
    else:
        print(item.rjust(4, '0'), end=":")
