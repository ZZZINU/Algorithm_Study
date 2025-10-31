from itertools import product
def solution(word):
    n = len(word)
    answer = 0
    vowel = ['A', 'E', 'I', 'O', 'U']
    dicts = []
    for i in range(1, 6):
        temp = list(product(vowel, repeat=i))
        for item in temp:
            dicts.append("".join(item))
    dicts.sort()
            
    # print(dicts)
        # dicts.append()
        
    for now in dicts:
        answer += 1
        if now == word:
            return answer
            
    
    return answer