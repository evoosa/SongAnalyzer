from song_analyzer.utils.histogram_utils import get_histogram_plot_file
from song_analyzer.song_parts.song import Song
import os

if __name__ == '__main__':

    lyrics_dir = r"C:\Users\User\Desktop\PS\SongAnalyzer\lyrics"  # FIXME - CMD LINE ARG
    output_path = r"C:\Users\User\Desktop\PS\SongAnalyzer\script_outputs\hist.png"

    print('\n[ Getting noun / adjectives ratios from songs.. ]\n')
    lyrics_files = [os.path.join(lyrics_dir, path) for path in os.listdir(lyrics_dir)]
    song_objects = [Song(lyrics) for lyrics in lyrics_files]
    noun_to_adj_ratios = [song.noun_to_adj_ratio for song in song_objects]

    print('\n[ Getting Histogram plot from ratios.. ]\n')
    get_histogram_plot_file(noun_to_adj_ratios, output_path)

    print('\n[ DONE ]\n')
