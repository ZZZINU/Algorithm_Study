from itertools import permutations, combinations

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for a in vowels:
        words.append(a)
        for e in vowels:
            words.append(a+e)
            for i in vowels:
                words.append(a+e+i)
                for o in vowels:
                    words.append(a+e+i+o)
                    for u in vowels:
                        words.append(a+e+i+o+u)
                        
    words.sort()
        
    
    return words.index(word) + 1
    
