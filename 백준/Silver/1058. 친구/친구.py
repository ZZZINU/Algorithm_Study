# 1058번: 염색체 (⚪실버_2)
N = int(input())

people = [[] for _ in range(N)]

for i in range(N):
    temp = input()

    for j in range(N):
        if temp[j] == 'Y':
            people[i].append(j)
max_count = 0

for i in range(N):
    friends = []
    friends.extend(people[i])

    for item in people[i]:


        for j in range(len(people[item])):
            if people[item][j] != i and people[item][j] not in friends:
                friends.append(people[item][j])

    if len(friends) > max_count:
        max_count = len(friends)

    
print(max_count)

