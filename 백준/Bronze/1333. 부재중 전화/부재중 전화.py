N, L, D = map(int, input().split())

time = 0
song = 0
is_playing = True
song_count = 0

while True:
    time += 1
    song += 1

    if is_playing == True and song == L:
        song = 0
        song_count += 1
        is_playing = False

    if is_playing == False and song == 5:
        song = 0
        is_playing = True

    if is_playing == False and time % D == 0:
        print(time)
        break
    
    if song_count >= N and time % D == 0:
        print(time)
        break 
