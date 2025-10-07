def solution(friends, gifts):
    answer = 0
    # [선물 준 횟수, 선물 받은 횟수]
    hash_map = {}
    answer_hash = {}
    gift_point_hash = {}
    gift_point = {}
    visited = []
    
    for friend_out in friends:
        hash_map[friend_out] = {}
        answer_hash[friend_out] = 0
        gift_point[friend_out] = 0
        gift_point_hash[friend_out] = [0, 0] # [준 선물, 받은 선물]
        for friend_in in friends:
            if friend_out != friend_in:
                hash_map[friend_out][friend_in] = 0
    
            
            
    for gift in gifts:
        # A -> B 선물 전달
        A, B = gift.split(" ")
        hash_map[A][B] += 1
        gift_point_hash[A][0] += 1
        gift_point_hash[B][1] += 1
    
    # 선물지수 측정
    for person in gift_point_hash:
        gift_point[person] = gift_point_hash[person][0] - gift_point_hash[person][1] 
        
        
    for give_person in friends:
        for received_person in friends:
            if give_person != received_person:
                
                # 기록이 없거나 같은 경우
                # hash_map[give_person][received_person] == 0
                if received_person not in visited and (hash_map[give_person][received_person] == hash_map[received_person][give_person]):
                    # print("기록이 없거나 같은 경우", give_person, received_person)
                    
                    
                    # 선물 지수가 같은 경우 패스
                    if gift_point[give_person] == gift_point[received_person]:
                        continue
                    
                    elif gift_point[give_person] < gift_point[received_person]:
                        answer_hash[received_person] += 1
                    else:
                        answer_hash[give_person] += 1
                        
                    
                    
                    
                
                # 기록이 있는 경우
                # if hash_map[give_person][received_person] > 0:
                else:
                    if received_person not in visited:
                    # print(give_person, "->", received_person, "기록 있음")
                        if hash_map[give_person][received_person] > hash_map[received_person][give_person]:
                            answer_hash[give_person] += 1
                        else:
                            answer_hash[received_person] += 1
                        

                        
        visited.append(give_person)
    
    # print(answer_hash)
                      
    answer = max(answer_hash.values())
    
                    
                
    

        
    return answer