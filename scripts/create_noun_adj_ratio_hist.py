from song_analyzer.utils.histogram_utils import get_histogram_plot_file
from song_analyzer.song_parts.song import Song
import os
from song_analyzer.config import BASE_DIR, LYRICS_DIR, SCRIPT_OUTPUTS_DIR
from datetime import datetime

if __name__ == '__main__':
    lyrics_dir = os.path.join(BASE_DIR, LYRICS_DIR)
    hist_plot_filename = "hist_plot-{}.png".format(datetime.now().strftime("%d-%m-%Y-%H-%M"))
    output_path = os.path.join(BASE_DIR, SCRIPT_OUTPUTS_DIR, hist_plot_filename)

    print('\n[ Getting noun / adjectives ratios from songs.. ]\n')
    lyrics_files = [os.path.join(lyrics_dir, path) for path in os.listdir(lyrics_dir)]
    song_objects = [Song(lyrics) for lyrics in lyrics_files]
    noun_to_adj_ratios = [song.noun_to_adj_ratio for song in song_objects]

    print('\n[ Getting Histogram plot from ratios.. ]\n')
    get_histogram_plot_file(noun_to_adj_ratios, output_path)

    print('\n[ DONE ]\n')
