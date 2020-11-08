#!/usr/bin/env python
import os

from song_analyzer.config import SCRIPT_OUTPUTS_DIR, HISTOGRAM_PLOT_FILENAME, LYRICS_FILE_PATHS
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.file_utils import create_dir_if_missing
from song_analyzer.utils.histogram_utils import gen_hist_plot_from_songs

if __name__ == '__main__':
    output_path = os.path.join(SCRIPT_OUTPUTS_DIR, HISTOGRAM_PLOT_FILENAME)
    create_dir_if_missing(SCRIPT_OUTPUTS_DIR)

    print('\n[ Getting Histogram plot.. ]')
    songs = [Song(lyrics_file) for lyrics_file in LYRICS_FILE_PATHS]
    gen_hist_plot_from_songs(output_path, songs)

    print('[ DONE ]')
    print('File location: {}\n'.format(output_path))
