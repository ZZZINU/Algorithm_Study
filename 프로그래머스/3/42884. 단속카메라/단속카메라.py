# 2025.11.07 -> GPT 사용
def solution(routes):
    routes.sort(key=lambda x:x[1])
    cameras = 0
    camera_pos = -10 ** 9
    
    for start, end in routes:
        if start > camera_pos:
            cameras += 1
            camera_pos = end
            
        
    return cameras