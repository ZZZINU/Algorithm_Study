import itertools, sys

n, m = map(int, input().split())

city_map = []
for i in range(n):
    temp = list(map(int, input().split()))
    city_map.append(temp)


def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []
    home_location_list = []
    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    min_distance_of_m_combinations = sys.maxsize
    for chicken_location_m_combination in chicken_location_m_combinations:
        distance = 0
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            for chicken_location in chicken_location_m_combination:
                min_home_chicken_distance = min(
                    min_home_chicken_distance,
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1]))
            distance += min_home_chicken_distance
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, distance)

    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map)) 
