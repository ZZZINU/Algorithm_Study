from itertools import permutations # 순열 - 라이브러리 사용

N, M = map(int, input().split()) # N, M 입력 (N개의 자연수 중에서 M개를 고른 수열)

nums = list(map(int, input().split())) # N개의 자연수 입력

result = permutations(nums, M) # 순열 구하기 (permutations(data, 선택할 개수))

result = sorted(set(result)) # 중복 원소 제거 -> set, 사전 순 정렬 -> sorted

# 각 수열은 공백으로 구분해서 출력
for num in result:
    print(' '.join(map(str, num)))