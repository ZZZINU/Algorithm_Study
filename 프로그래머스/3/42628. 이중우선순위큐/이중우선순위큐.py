import heapq
def solution(operations):
    heap = []
    heap_max = []
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            heapq.heappush(heap, num)
            heapq.heappush(heap_max, -num)
        
        elif command == 'D':
            if num == 1 and heap_max:
                max_pop = heapq.heappop(heap_max)
                heap.remove(-max_pop)
            
            elif num == -1 and heap:
                min_pop = heapq.heappop(heap)
                heap_max.remove(-min_pop)
    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]
    
