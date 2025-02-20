# A - Z : 65 - 90
# a - z : 97 - 122

def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            answer += " "
            continue   
        
        num = ord(i) + n
        
        if 'A' <= i <= 'Z':
            if num > ord('Z'):
                num -= 26
        
        elif 'a' <= i <= 'z':
            if num > ord('z'):
                num -= 26

        char = chr(num)
        answer += char
    
    
    return answer