def solution(id_list, report, k):
    answer = []
    report_count = {user: 0 for user in id_list}
    user_reports = {user: set() for user in id_list}
    
    for entry in report:
        reporter, reported = entry.split()
        if reported not in user_reports[reporter]:
            user_reports[reporter].add(reported)
            report_count[reported] += 1
    # print(report_count)
    # print(user_reports)
    
    banned_users = []
    
    for item in report_count:
        if report_count[item] >= k:
            banned_users.append(item)
    
    for reporter in user_reports:
        count = 0
        for ban in banned_users:
            if ban in user_reports[reporter]:
                count += 1
        answer.append(count)
    
    return answer

