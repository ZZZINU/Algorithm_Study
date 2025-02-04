def solution(genres, plays):
    answer = []
    song = {}
    total_song = {}
    
    for i in range(len(genres)):
        name = genres[i]
        if name not in song:
            total_song[name] = plays[i]
            song[name] = [[plays[i], i]]
        else:
            total_song[name] += plays[i]
            song[name].append([plays[i], i])
    
    total_song = sorted(total_song.items(), key=lambda item:item[1], reverse=True)
    
    
    for i in range(len(song)):
        name = total_song[i][0]
        # sorted_song = sorted(song[name], reverse=True)
        sorted_song = sorted(song[name], key=lambda x: (-x[0], x[1]))

        if len(sorted_song) == 1:
            answer.append(sorted_song[0][1])
        else:
            answer.append(sorted_song[0][1])
            answer.append(sorted_song[1][1])
        

    return answer