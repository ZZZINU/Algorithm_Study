# 2578번: 빙고 (⚪실버_4)
bingo = []
bingo_case= [[0,1,2,3,4], [5,6,7,8,9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24], 
             [0, 5, 10, 15, 20], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], 
             [0, 6, 12, 18, 24,],[4, 8, 12, 16, 20]]

for i in range(5):
    temp = list(map(int, input().split()))
    bingo.extend(temp)


called_num = []

for i in range(5):
    temp = list(map(int, input().split()))
    called_num.extend(temp)


bingo_index = []
order = 0

for num in called_num:
    index = bingo.index(num)
    bingo_index.append(index)
    order += 1
    
    if len(bingo_index) >= 12:
        bingo_count = 0
        for i in range(len(bingo_case)):
            if all (element in bingo_index for element in bingo_case[i]):
                bingo_count += 1
            
            if bingo_count == 3:
                print(order)
                exit()
    
