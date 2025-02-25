def solution(s):
    answer = ''
    num = 0
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
            num = 0
        elif num % 2 == 0:
            answer += s[i].upper()
            num += 1
        else:
            answer += s[i].lower()
            num += 1
    return answer