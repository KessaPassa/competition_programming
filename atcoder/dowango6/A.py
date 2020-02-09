class Music:
    def __init__(self, name, time):
        self.name = name
        self.time = int(time)


n = int(input())
data = [(input().split()) for _ in range(n)]
music_list = [Music(d[0], d[1]) for d in data]
x = input()

start_music = None
for music in music_list:
    if music.name == x:
        start_music = music
        break

if start_music is None:
    print(0)
else:
    index = music_list.index(start_music)
    skipped_list = music_list[index+1:]

    skipped_time = 0
    for music in skipped_list:
        skipped_time += music.time
    print(skipped_time)
