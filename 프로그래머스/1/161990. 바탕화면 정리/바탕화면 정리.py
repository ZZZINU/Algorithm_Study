def solution(wallpaper):
    width=len(wallpaper)
    height=len(wallpaper[0])
    answer = []
    points_i = []
    points_j = []
    for i in range(width):
        for j in range(height):
             if wallpaper[i][j] == "#":
                    points_i.append(i)
                    points_j.append(j)
    
    answer.append(min(points_i))
    answer.append(min(points_j))
    answer.append(max(points_i) + 1)
    answer.append(max(points_j) + 1)
    
    return answer