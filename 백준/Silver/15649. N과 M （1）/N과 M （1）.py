from itertools import permutations

N, M = map(int, input().split())

result = list(permutations(range(1, N+1), M))

for item in result:
    print(' '.join(map(str, item)))
