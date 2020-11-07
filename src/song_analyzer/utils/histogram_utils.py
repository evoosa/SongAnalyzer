import os
from song_analyzer.song_parts.song import Song

# TEST
lyrics_dir = r"C:\Users\evoosa\Desktop\JobShit\SongAnalyzer\lyrics"
lyrics_files = [os.path.join(lyrics_dir, f) for f in os.listdir(lyrics_dir)]

song_objects = [Song(lyrics) for lyrics in lyrics_files]
for s in song_objects:
    for sen in s.sentences:
        for w in sen.words:
            print(w.data, w.pos)

noun_to_adj_ratios = [song.noun_to_adj_ratio for song in song_objects]
print(noun_to_adj_ratios)
# get the frequency of the ratios
# print nicely
