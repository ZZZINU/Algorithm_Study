from itertools import combinations
import math

def solution(nums):
    answer = 0
    combinations_list = list(combinations(nums, 3))
    sum_list = []

    for item in combinations_list:
        num = sum(item)
        sum_list.append(num)
        count = 0
        num_sqrt = math.ceil(math.sqrt(num))
        # print("num", num)
        # print("num_sqrt", num_sqrt)
        for i in range(2, num_sqrt+1):
            # print(i)
            if num % i == 0:
                break
        else:     
            # print("소수")
            answer += 1
        
    
#     sum_set = set(sum_list)
    
#     for item in sum_set
    
    return answer