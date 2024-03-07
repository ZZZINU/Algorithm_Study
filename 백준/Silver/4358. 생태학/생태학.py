dictionary = {}
count = 0

while True:
    if len(dictionary) > 10000 or count > 1000000:
        break
        
    try:
        name = input()
    
        if len(name) <= 30 and name.isascii() and name != "": # 종 이름은 30자 이하
            count += 1
            if name in dictionary:
                dictionary[name] += 1
            else:
                dictionary[name] = 1
                
        else:
            print("종 이름은 30글자 이하입니다.")    
    except:
        break

    
dictionary = sorted(dictionary.items())
length = len(dictionary)

if count != 0:
    for key, value in dictionary:
        ratio = "{:.4f}".format(float(value / count * 100))
        print(f"{key} {ratio}")
        # print("{:.4f}".format(ratio))  