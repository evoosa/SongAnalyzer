import os
from datetime import datetime

from song_analyzer.config import BASE_DIR, LYRICS_DIR, SCRIPT_OUTPUTS_DIR, HISTOGRAM_PLOT_FILENAME
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.histogram_utils import generate_histogram_plot_file
from song_analyzer.utils.song_analysis_utils import get_pos_entities_from_sentences

if __name__ == '__main__':
    lyrics_dir = os.path.join(BASE_DIR, LYRICS_DIR)
    hist_plot_filename = datetime.now().strftime("%d-%m-%Y-%H-%M") + '-' + HISTOGRAM_PLOT_FILENAME
    output_path = os.path.join(BASE_DIR, SCRIPT_OUTPUTS_DIR, hist_plot_filename)

    print('\n[ Getting noun / adjectives ratios from songs.. ]\n')
    lyrics_files = [os.path.join(lyrics_dir, path) for path in os.listdir(lyrics_dir)]

    noun_to_adj_ratios = []
    for lyrics_file in lyrics_files:
        print('[ Getting ratio for: {}.. ]'.format(lyrics_file))
        song_obj = Song(lyrics_file)
        song_pos_entities = get_pos_entities_from_sentences(song_obj.sentences)
        noun_to_adj_ratios.append(song_pos_entities['noun_to_adjective_ratio'])

    print('\n[ Getting Histogram plot from ratios.. ]\n')
    generate_histogram_plot_file(noun_to_adj_ratios, output_path)

    print('[ DONE ]')
    print('File location: {}'.format(output_path))
