# 1747번: 소수&팰린드롬(⚪실버_1)

N = int(input()) # N 입력

num = 1 # num은 N부터 1씩 올려가면서 검사

if 1<= N <= 1000000: # N (1 ≤ N ≤ 1,000,000)
    if N != 1: # 1일 때는 예외 -> 1은 소수가 아니므로 num을 바로 2로 넘김 
        num = N-1 # num = N-1로 한 이유는 while문에서 +1을 먼저 해주기 때문

    while True: # 조건을 만족하는 수 찾을 때까지 반복
        num += 1 # num은 1씩 증가
        string = str(num) # num을 문자로 바꿔서 저장
        if string == string[::-1]: # 1. 팰린드롬 검사 : 원래 문자열과 뒤집은 문자열이 동일한지를 확인하는 조건
            for i in range(2, int(num**0.5) + 1): # 2. 소수인지 검사 : 그 수의 제곱근까지만 확인하면 됨
                if num%i==0: # 1과 자신을 제외한 다른 약수가 있다면
                    break # 다음 num 으로 넘어가기
            
            else: # 위의 조건 (1 과 2)를 통과했다면
                print(num) # 해당 num을 출력
                break # 반복문 종료