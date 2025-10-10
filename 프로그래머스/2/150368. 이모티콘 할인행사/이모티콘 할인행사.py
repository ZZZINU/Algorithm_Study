from itertools import product

def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    m = len(emoticons)
    
    # 가입자 수, 매출액 최대치
    best_sub = -1
    best_rev = -1
    
    # 미리 할인별 가격 테이블 계산
    price_table = []
    for d in discounts:
        rate = 100 - d
        price_table.append([e * rate // 100 for e in emoticons])
    
    # print(price_table)
    for ds in product(range(4), repeat=m):
        # print(ds)
        subs = 0
        rev = 0
        
        # 각 사용자 처리
        for min_pct, min_price in users:
            cost = 0
            # 해당 사용자 기준 이상 할인된 것만 담기
            for j in range(m):
                if discounts[ds[j]] >= min_pct:
                    cost += price_table[ds[j]][j]
                # 이미 기준 금액 넘으면 가입 전환
                if cost >= min_price:
                    subs += 1
                    cost = 0
                    break
            rev += cost
        
        if subs > best_sub or (subs == best_sub and rev > best_rev):
            best_sub, best_rev = subs, rev
            
    
    return [best_sub, best_rev]