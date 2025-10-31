def solution(brown, yellow):
    answer = []
    x_y_sum = int((brown-4) / 2)
    # print(x_y_sum)
    x_y_multi = yellow
    
    for i in range(1, x_y_sum+1):
        x = i
        y = x_y_sum-x
        if x * y == x_y_multi:
            answer.append(max(x, y) + 2)
            answer.append(min(x, y) + 2)
            return answer
