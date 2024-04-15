import math
N = int(input())
nums = []
for _ in range(N):
    temp = list(map(int, input()))
    nums.append(temp)


for _ in range(int(math.log(N, 2))):
    new_nums = []
    length = len(nums)

    for i in range(0, length, 2):
        row = []
        for j in range(0, length, 2):
            if nums[i][j] == nums[i][j+1] == nums[i+1][j] == nums[i+1][j+1]:
                if isinstance(nums[i][j], list):
                    if (len(nums[i][j]) == 1):
                        row.append(nums[i][j])
                    else:
                        temp = [nums[i][j], nums[i][j+1], nums[i+1][j], nums[i+1][j+1]]
                        row.append(temp)
                else:
                    row.append(nums[i][j])
            else:
                temp = [nums[i][j], nums[i][j+1], nums[i+1][j], nums[i+1][j+1]]
                row.append(temp)
        new_nums.append(row)

    nums = new_nums


def unwrap_list(nums):
    if isinstance(nums, list):
        if len(nums) == 1:
            return unwrap_list(nums[0])
        else:
            return [unwrap_list(item) for item in nums]
    return nums


nums = unwrap_list(nums)



def print_nums(nums):
    if isinstance(nums, list):
        print("(", end="")
        for item in nums:
            print_nums(item)
        print(")", end="")
    else:
        print(nums, end="")

print_nums(nums)
     