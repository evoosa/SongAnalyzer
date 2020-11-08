import csv
import os

from song_analyzer.config import SCRIPT_OUTPUTS_DIR, CSV_COLUMNS, HISTOGRAM_PLOT_FILENAME, LYRICS_FILE_PATHS
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.file_utils import create_dir_if_missing, create_csv_with_field_names, update_pos_stats_file
from song_analyzer.utils.histogram_utils import generate_histogram_plot_file
from song_analyzer.utils.song_analysis_utils import get_pos_entities_from_sentences, get_song_length_stats

if __name__ == '__main__':

    print('\n[ Getting all songs info.. ]\n')
    song_objects = [Song(lyrics) for lyrics in LYRICS_FILE_PATHS]

    artists = {}
    for song_obj in song_objects:
        artist_name = song_obj.metadata['artist']
        artist_output_dir = os.path.join(SCRIPT_OUTPUTS_DIR, artist_name)
        create_dir_if_missing(artist_output_dir)

        if artist_name not in artists.keys():
            artists[artist_name] = {
                'songs': [],
                'output_dir': artist_output_dir
            }

            create_csv_with_field_names(os.path.join(artist_output_dir, 'general_statistics.csv'), CSV_COLUMNS)

        artists[artist_name]['songs'].append(song_obj)

        print('\n[[ {} ]]'.format(song_obj.metadata['name']))

        print('[ writing POS entities ]')
        update_pos_stats_file(os.path.join(artist_output_dir, 'pos_statistics.txt'), song_obj)

        print('[ writing general stats ]')
        with open(os.path.join(artist_output_dir, 'general_statistics.csv'), 'a', newline='',
                  encoding='utf-8') as general_stats_file:
            len_stats = get_song_length_stats(song_obj.sentences)
            writer = csv.DictWriter(general_stats_file, fieldnames=CSV_COLUMNS)
            writer.writerow(len_stats)

    print('\n[[ Create POS histograms for all artists ]]')
    for artist in artists.values():
        noun_to_adj_ratios = []
        output_file_path = os.path.join(artist['output_dir'], HISTOGRAM_PLOT_FILENAME)
        for song_obj in artist['songs']:
            song_pos_entities = get_pos_entities_from_sentences(song_obj.sentences)
            noun_to_adj_ratios.append(song_pos_entities['noun_to_adjective_ratio'])
        generate_histogram_plot_file(noun_to_adj_ratios, output_file_path)
    print('[[ DONE ]]')
