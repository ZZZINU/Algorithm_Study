def solution(array):
    answer = 0
    dict = {}
    for item in array:
        if item in dict:
            dict[item] += 1 
        else:
            dict[item] = 1
            
    max_value = max(dict.values())
    
#     count = 0
#     for key in dict:
#         if dict[key] == temp:
#             count += 1
    array = []
    for key, value in dict.items():
        if value == max_value:
            array.append(key)
            
    
    if len(array) > 1:
        return -1
    else:
        return array[0]
            

          
    
    
    
