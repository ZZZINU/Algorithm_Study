def solution(numbers, hand):
    answer = ''
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    phone_index = {
        1: [0,0], 2: [0,1], 3: [0,2],
        4: [1,0], 5: [1,1], 6: [1,2],
        7: [2,0], 8: [2,1], 9: [2,2],
        '*': [3,0], 0: [3,1], '#': [3,2],   
    }
    
    

    left = '*'
    right = '#'

    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left = num
        elif num in [3, 6, 9]:
            answer += "R"
            right = num
        else:
            x, y = phone_index[num]
            left_x, left_y = phone_index[left]
            right_x, right_y = phone_index[right]
            print()
            
            left_diff = abs(left_x-x) + abs(left_y-y)
            right_diff = abs(right_x-x) + abs(right_y-y)
            
            if left_diff < right_diff:
                answer += "L"
                left = num
            elif right_diff < left_diff:
                answer += "R"
                right = num
            else:
                if hand == 'right':
                    answer += "R"
                    right = num
                else:
                    answer += "L"
                    left = num

    return answer