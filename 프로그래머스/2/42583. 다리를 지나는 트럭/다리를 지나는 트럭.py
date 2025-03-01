from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    # print("bridge", bridge)
    
    now_weight = 0
    while truck_weights :
        time += 1
        now_weight -= bridge.popleft()

        if now_weight + truck_weights[0] <= weight:
            now_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
        # print(bridge)
            
    time += bridge_length
    return time