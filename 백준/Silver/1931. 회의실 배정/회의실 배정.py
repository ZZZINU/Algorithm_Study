N = int(input())

meetings = []
count = 0

for i in range(N):
    start, end = map(int, input().split())
    meetings.append([start, end])
    
meetings.sort(key=lambda x: (x[1], x[0]))

prevEnd = 0

for nextStart, nextEnd in meetings:  
    if nextStart >= prevEnd:
        count += 1
        prevEnd = nextEnd

print(count)
