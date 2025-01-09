from collections import Counter

def solution(X, Y):
    answer = ''
    count_X = Counter(X)
    count_Y = Counter(Y)

    common_dict = {}
    
    for count in count_X:
        if count in count_Y:
            common_dict[count] = min(count_X[count], count_Y[count])
            
 

    keys = common_dict.keys()
    keys = sorted(keys, reverse=True)
    
   
    for key in keys:
        temp = key * common_dict[key]
        answer += temp
    
    
    if not answer:
        answer = "-1"
    elif answer == "0" * len(answer):
        answer = "0"
    
        
            
    return answer