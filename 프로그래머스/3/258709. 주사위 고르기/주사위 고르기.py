from itertools import combinations
from bisect import bisect_left

def _all_sums(dice, indices):
    # indices에 해당하는 주사위들을 굴려 나올 수 있는 모든 합 리스트
    sums = [0]
    for i in indices:
        faces = dice[i]
        temp = []
        for f in faces:
            for s in sums:
                new_sum = s + f
                temp.append(new_sum)
        
        sums = temp
        # print("??", indices, sums)
    return sums
            
    

def solution(dice):
    n = len(dice)
    half = n // 2
    
    best_combo = None
    best_wins = -1
    
    # n개 중 half개 고르는 모든 조합
    for a_combo in combinations(range(n), half):
        a_set = set(a_combo)
        b_combo = [i for i in range(n) if i not in a_set]
        
        # A/B의 가능한 모든 합
        arrA = _all_sums(dice, a_combo)
        arrB = _all_sums(dice, b_combo)
        arrB.sort()
        
        # A의 각 합 x에 대해, x보다 작은 B의 합 개수 누적(A가 이긴 횟수)
        wins = 0
        for x in arrA:
            wins += bisect_left(arrB, x)
        
        if wins > best_wins or (wins == best_wins and (best_combo is None or list(a_combo) < list(best_combo))):
            best_wins = wins
            best_combo = a_combo
    
    
    
    return [i+1 for i in best_combo]