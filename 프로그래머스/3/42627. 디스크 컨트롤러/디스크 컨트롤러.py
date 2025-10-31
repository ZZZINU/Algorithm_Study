import heapq

def solution(jobs):
    # jobs: [[s, l], ...]
    n = len(jobs)
    jobs = sorted([(s, l, i) for i, (s, l) in enumerate(jobs)])  # 요청시각 기준
    i = 0           # 아직 힙에 못 넣은 작업의 포인터
    t = 0           # 현재 시각
    total_turn = 0  # 반환시간 합
    heap = []       # (l, s, idx)

    while i < n or heap:
        # 현재 시각까지 도착한 작업을 모두 push
        while i < n and jobs[i][0] <= t:
            s, l, idx = jobs[i]
            heapq.heappush(heap, (l, s, idx))
            i += 1

        if heap:
            l, s, idx = heapq.heappop(heap)
            t += l
            total_turn += t - s
        else:
            # 대기 작업이 없다면 다음 도착 시각으로 점프
            s, l, idx = jobs[i]
            t = max(t, s)
            # 이제 이 작업을 힙에 넣고 즉시 루프에서 처리될 수 있게 함
            heapq.heappush(heap, (l, s, idx))
            i += 1

    return total_turn // n
