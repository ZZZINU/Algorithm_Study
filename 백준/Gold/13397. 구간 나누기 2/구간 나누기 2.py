# 13397번: 구간 나누기 2

def isValid(mid):
    low = num[0]
    high = num[0]
    section = 1

    for i in num:
        if high < i:
            high = i
        if low > i:
            low = i
        
        if high - low > mid:
            section += 1
            low = i
            high = i
    
    return M >= section


N, M = map(int, input().split())
num = list(map(int, input().split()))

left, right = 0, max(num)
result = right

while left <= right:
    mid = (left+right)//2

    if isValid(mid):
        right = mid-1
        result = min(mid, result)
    else:
        left = mid + 1

print(result)
