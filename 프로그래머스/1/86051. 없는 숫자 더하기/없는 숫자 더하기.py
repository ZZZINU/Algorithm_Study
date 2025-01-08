def solution(numbers):
    answer = 0
    dict = {}
    
    for i in range(10):
        dict[i] = 0
        
    for num in numbers:
        dict[num] += 1
        
    for num in dict:
        print(num)
        if dict[num] == 0:
            answer += num

    
    return answer