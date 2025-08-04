from collections import deque
def solution(prices):
    # 이 부분을 채워주세요!
    prices_queue = deque(prices)
    result = []
    while prices_queue:
        price_not_fall_period = 0
        current_price = prices_queue.popleft()
        for next_price in prices_queue:
            if current_price <= next_price:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break
        result.append(price_not_fall_period)

    return result