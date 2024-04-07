asset = int(input())
price = list(map(int, input().split()))

BNP_asset = 0 # 자산
BNP_cash = asset # 현금
BNP_stock = 0 # 주식 수

# 1. BMP
for i in range(14):
    if BNP_cash >= price[i]:
        cnt = BNP_cash // price[i]
        BNP_stock += cnt # 주식 수 계산
        BNP_cash = BNP_cash % price[i]  # 남은 현금 계산
        
BNP_asset = BNP_stock * price[-1] + BNP_cash

# 2. TIMING
TIMING_asset = 0 # 자산
TIMING_cash = asset # 현금
TIMING_stock = 0 # 주식 수

increase_cnt = 0
decrease_cnt = 0

for i in range(1, 14):
    if price[i-1] < price[i]: # 전일 대비 상승
        decrease_cnt = 0 
        increase_cnt += 1 # 상승 카운트 1 증가
    elif price[i-1] > price[i]: # 전일 대비 하락
        increase_cnt = 0
        decrease_cnt += 1
    else:
        increase_cnt = 0
        decrease_cnt = 0 
    
    
    if increase_cnt >= 3:
        if TIMING_stock > 0:
            TIMING_cash = price[i] * TIMING_stock
            TIMING_stock = 0
        
    elif decrease_cnt >= 3:
        if TIMING_cash >= price[i]:
            cnt = TIMING_cash // price[i]
            TIMING_stock += cnt # 주식 수 계산
            TIMING_cash = TIMING_cash % price[i] # 남은 현금 계산
            
        
TIMING_asset = TIMING_stock * price[-1] + TIMING_cash

if BNP_asset > TIMING_asset:
    print("BNP")
elif BNP_asset < TIMING_asset:
    print("TIMING")
else:
    print("SAMESAME")