import math

def sieve_of_eratosthenes(end):
    primes = [True] * (end + 1)
    primes[0] = primes[1] = False
    
    # 주어진 범위의 제곱근까지만 반복
    for i in range(2, math.isqrt(end) + 1):
        if primes[i]:
            # i의 배수들을 모두 소수가 아닌 것으로 표시
            for j in range(i * i, end + 1, i):
                primes[j] = False
    
    # 소수들의 목록 반환
    return [i for i in range(2, end + 1) if primes[i]]

# 왼쪽 범위 A와 오른쪽 범위 B 입력
min_num, max_num = map(int, input().split())

# 주어진 범위 내의 모든 소수 찾기
primes = sieve_of_eratosthenes(math.isqrt(max_num))

count = 0

# 주어진 범위 내의 각 소수의 거듭제곱수 개수 세기
for prime in primes:
    power = 2
    while prime ** power <= max_num:
        if prime ** power >= min_num:
            count += 1
        power += 1

print(count)
