from itertools import combinations

def make_all_cases(user_info_array):
    all_cases_from_user = []
    for i in range(5):
        for combination in combinations([0, 1, 2, 3], i):
            case = ""
            for j in range(4):
                if j not in combination:
                    case += user_info_array[j]
                else:
                    case += "-"
            all_cases_from_user.append(case)
    return all_cases_from_user

def get_lower_bound(target, array):
    current_min = 0
    current_max = len(array)
    
    while current_min < current_max:
        currnet_guess = (current_min + current_max) // 2
        if array[currnet_guess] >= target:
            current_max = currnet_guess
        else:
            current_min = currnet_guess + 1
    
    return current_max
    

def solution(info, query):
    answer = []
    all_cases_from_users = {}
    for user_info in info:
        user_info_array = user_info.split()
        all_cases_from_user = make_all_cases(user_info_array)
        for case in all_cases_from_user:
            if case not in all_cases_from_users.keys():
                all_cases_from_users[case] = [int(user_info_array[4])]
            else:
                all_cases_from_users[case].append(int(user_info_array[4]))
    
    for key in all_cases_from_users.keys():
        all_cases_from_users[key].sort()
    
    
    for query_info in query:
        query_info_array = query_info.split()
        case = query_info_array[0] + query_info_array[2] + query_info_array[4] + query_info_array[6]
        if case in all_cases_from_users.keys():
            target_users = all_cases_from_users[case]
            answer.append(
                len(target_users) - get_lower_bound(int(query_info_array[7]), target_users)
            )
        else:
            answer.append(0)
        
                
    return answer