from itertools import combinations

def solution(numbers):
    answer = []
    nums_set = []
    nums = list(combinations(numbers, 2))
    for i in nums:
        print(i)
        x, y = i
        temp = x+y
        nums_set.append(temp)
    answer = list(set(nums_set))
    answer.sort()
    return answer