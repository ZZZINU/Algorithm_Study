import heapq
import sys

input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print("0")
    else:
        heapq.heappush(heap, -x)


