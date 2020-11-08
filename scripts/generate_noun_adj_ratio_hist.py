import os

from song_analyzer.config import SCRIPT_OUTPUTS_DIR, HISTOGRAM_PLOT_FILENAME, LYRICS_FILE_PATHS, NOW
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.file_utils import create_dir_if_missing
from song_analyzer.utils.histogram_utils import generate_histogram_plot_file, gen_hist_plot_from_songs
from song_analyzer.utils.song_analysis_utils import get_pos_entities_from_sentences

if __name__ == '__main__':
    plot_filename = NOW + '-' + HISTOGRAM_PLOT_FILENAME
    output_path = os.path.join(SCRIPT_OUTPUTS_DIR, plot_filename)
    create_dir_if_missing(SCRIPT_OUTPUTS_DIR)

    print('\n[ Getting noun / adjective ratios from songs.. ]\n')
    songs = [Song(lyrics_file) for lyrics_file in LYRICS_FILE_PATHS]

    print('\n[ Getting Histogram plot from ratios.. ]\n')
    gen_hist_plot_from_songs(output_path, songs)

    print('[ DONE ]')
    print('File location: {}'.format(output_path))
