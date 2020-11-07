import os
from song_analyzer.song_parts.song import Song
# TEST
lyrics_dir = r"C:\Users\evoosa\Desktop\JobShit\SongAnalyzer\lyrics"
lyrics_files = [os.path.join(lyrics_dir, f) for f in os.listdir(lyrics_dir)]
print(lyrics_files)

song_objects = [Song(lyrics)]
# get Song object and put in list
# get the frequency of the ratios
# print nicely
