def solution(elements):

    n = len(elements)
    result = set()
    
    for i in range(1, n+1): # 부분 수열의 길이
        left = 0
        right = i-1
        sum = 0
        
        for j in range(i): # 초기 윈도우 합: elements[0..i-1]
            sum += elements[j]
        result.add(sum)
        
        # 슬라이딩 윈도우: 시작점을 1칸씩 민다(총 n-1번 이동해서 합 n개 생성)
        for j in range(1, n):
            right = (right+1) % n  # 원형이므로 모듈로로 한 칸 전진
            sum = sum - elements[left] + elements[right] # 윈도우 갱신
            left = (left+1) % n
            result.add(sum)

    return len(result)