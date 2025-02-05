def solution(array, commands):
    answer = []
    
    for command in commands:
        start, end, idx = command
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[idx-1])

    return answer