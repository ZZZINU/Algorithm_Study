def solution(s):
    answer = []
    dictionary = {}
    for i in range(len(s)):
        text = s[i]
        if text in dictionary:
            answer.append(i - dictionary[text])
        else:
            answer.append(-1)
        dictionary[text] = i
            
    return answer