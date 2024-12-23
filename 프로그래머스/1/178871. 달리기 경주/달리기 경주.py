def solution(players, callings):
#     answer = players
#     count = {}
#     for i in range (len(callings)):
#         if callings[i] not in count:
#             count[callings[i]] = 1
#         else:
#             count[callings[i]] += 1
    
#     print(count)
    
#     for i in range(len(players)):
#         if players[i] in count:
#                 print(count)

            # temp = answer[i]
            # answer[i] = answer[i-count[players[i]]]
            # answer[i-count[players[i]]] = temp
    
  

    # for i in range (len(callings)):
    #     for j in range(len(players)):
    #         if players[j] == callings[i]:
    #             temp = players[j]
    #             players[j] = players[j-1]
    #             players[j-1] = temp
    #             break
    
    answer = {}
    
    for i in range(len(players)):
        # print(players, i)
        answer[players[i]] = i
    # print(answer)
    
    for i in range(len(callings)):
        # print("callings[i]", callings[i])
        my_idx = answer[callings[i]]
        front = players[answer[callings[i]]-1] # poe
        front_idx = answer[front]
        # print("my_idx", my_idx) 
        # print("front", front) 
        # print("front_idx", front_idx) 
        
        temp = players[my_idx]
        players[my_idx] = players[front_idx]
        players[front_idx] = temp
        
        answer[callings[i]] -= 1
        answer[front] += 1
        

        # print("---------------------")
        # answer[callings[i]]
        
    # print(answer)   
    return players