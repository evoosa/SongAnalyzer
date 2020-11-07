import os
from song_analyzer.song_parts.song import Song
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# TEST
lyrics_dir = r"C:\Users\evoosa\Desktop\JobShit\SongAnalyzer\lyrics"
lyrics_files = [os.path.join(lyrics_dir, f) for f in os.listdir(lyrics_dir)]

song_objects = [Song(lyrics) for lyrics in lyrics_files]

# for s in song_objects:
#     for sen in s.sentences:
#         for w in sen.words:
#             print(w.data, w.pos)

noun_adj_ratios = [song.noun_to_adj_ratio for song in song_objects]
print(noun_adj_ratios)

noun_adj_ratios_np = pd.Series(noun_adj_ratios)
noun_adj_ratios_np.plot.hist(grid=True, bins='auto', rwidth=0.9,
                   color='#607c8e')
plt.title('Commute Times for 1,000 Commuters')
plt.xlabel('noun/adjective ratio')
plt.ylabel('number of songs')
plt.grid(axis='y', alpha=0.75)

# TODO - one for all artists, one for specific artists
