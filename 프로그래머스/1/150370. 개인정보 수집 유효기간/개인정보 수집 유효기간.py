def solution(today, terms, privacies):
    
    # 1) 약관 종류 -> 개월 수 해시
    term_months = {}
    for t in terms:
        kind, months = t.split()
        term_months[kind] = int(months)
    
    # 날짜 -> 일수 (기준: 2000-01-01을 day 1로 잡아도 )
    def to_days(date_str):
        y, m , d = map(int, date_str.split("."))
        return ((y-2000) * 12 + (m-1)) * 28 + d
    
    today_days = to_days(today)
    answer = []
    
    for i, item in enumerate(privacies, start=1):
        date_str, kind = item.split()
        collected = to_days(date_str)
        expire = collected + term_months[kind] * 28 - 1
        
        if today_days > expire:
            answer.append(i)
    
    
    return answer