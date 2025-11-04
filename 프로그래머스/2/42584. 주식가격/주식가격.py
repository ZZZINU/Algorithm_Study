from collections import deque
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i, price in enumerate(prices):
        # 가격이 낮아진 경우
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = n - j - 1
    
    
    return answer