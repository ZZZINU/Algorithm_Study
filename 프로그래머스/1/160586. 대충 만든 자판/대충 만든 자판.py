def solution(keymap, targets):
    answer = []
    keymap_dict = {}
    
    for key in keymap:
        for i in range(len(key)):
            if key[i] in keymap_dict:
                keymap_dict[key[i]] = min(keymap_dict[key[i]], i + 1)
            else:
                keymap_dict[key[i]] = i + 1

    
    for target in targets:
        count = 0
        for i in range(len(target)):
            if target[i] in keymap_dict:
                count += keymap_dict[target[i]]
            else:
                count = -1
                break
                
        
        answer.append(count)
        
    return answer