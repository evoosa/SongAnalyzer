import os
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.song_utils import
# TEST
lyrics_dir = r"C:\Users\evoosa\Desktop\JobShit\SongAnalyzer\lyrics"
lyrics_files = [os.path.join(lyrics_dir, f) for f in os.listdir(lyrics_dir)]
print(lyrics_files)

song_objects = [Song(lyrics) for lyrics in lyrics_files]
map(lambda song: song.get_words_pos(), song_objects)

songs_noun_to_adj_ratio = []
# get the frequency of the ratios
# print nicely
