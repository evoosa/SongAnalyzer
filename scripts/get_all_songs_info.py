import os
from song_analyzer.config import BASE_DIR, LYRICS_DIR, SCRIPT_OUTPUTS_DIR, CSV_COLUMNS, HISTOGRAM_PLOT_FILENAME
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.histogram_utils import generate_histogram_plot_file
from song_analyzer.utils.song_analysis_utils import get_pos_entities_from_sentences, get_song_length_stats
import csv

if __name__ == '__main__':  # TODO - verbosity!!
    lyrics_dir = os.path.join(BASE_DIR, LYRICS_DIR)
    output_dir = os.path.join(BASE_DIR, SCRIPT_OUTPUTS_DIR)

    print('\n[ Getting all songs info.. ]\n')
    lyrics_files = [os.path.join(lyrics_dir, path) for path in os.listdir(lyrics_dir)]
    song_objects = [Song(lyrics) for lyrics in lyrics_files]

    artists = {}
    for song_obj in song_objects:
        # Get Artist object
        artist_name = song_obj.metadata['artist']
        artist_output_dir = os.path.join(BASE_DIR, SCRIPT_OUTPUTS_DIR, artist_name)

        if not os.path.exists(artist_output_dir):
            os.makedirs(artist_output_dir)

        if artist_name not in artists.keys():
            artists[artist_name] = {
                'songs': [],
                'output_dir': artist_output_dir
            }

            # create general stats CSV file
            with open(os.path.join(artist_output_dir, 'general_statistics.csv'), 'w', newline='',
                      encoding='utf-8') as general_stats_file:
                writer = csv.DictWriter(general_stats_file, fieldnames=CSV_COLUMNS)
                writer.writeheader()

        artists[artist_name]['songs'].append(song_obj)
        print('\n[[ {} ]]'.format(song_obj.metadata['name']))

        print('[ writing POS entities ]')
        with open(os.path.join(artist_output_dir, 'pos_statistics.txt'), 'a') as pos_file:
            pos_entities = get_pos_entities_from_sentences(song_obj.sentences)
            pos_file.write('\n-- {} --\n'.format(song_obj.metadata['name']))
            pos_file.write('\n[ NOUNS ]\n')
            map(lambda noun: pos_file.write(noun + '\n'), set(pos_entities['nouns']))
            pos_file.write('\n[ ADJECTIVES ]\n')
            map(lambda adjective: pos_file.write(adjective + '\n'), set(pos_entities['adjectives']))
            pos_file.write('\nnoun/adjective ratio: {0} / {1} = {2}\n'.format(len(pos_entities['nouns']),
                                                                              len(pos_entities['adjectives']),
                                                                              pos_entities['noun_to_adjective_ratio']))
        print('[ writing general stats ]')
        with open(os.path.join(artist_output_dir, 'general_statistics.csv'), 'a', newline='',
                  encoding='utf-8') as general_stats_file:
            len_stats = get_song_length_stats(song_obj.sentences)
            writer = csv.DictWriter(general_stats_file, fieldnames=CSV_COLUMNS)
            writer.writerow(len_stats)

    # Create POS diagram for all artists
    print('\n[[ Create POS histograms for all artists ]]')
    for artist in artists.values():
        noun_to_adj_ratios = []
        output_file_path = os.path.join(artist['output_dir'], HISTOGRAM_PLOT_FILENAME)
        for song_obj in artist['songs']:
            song_pos_entities = get_pos_entities_from_sentences(song_obj.sentences)
            noun_to_adj_ratios.append(song_pos_entities['noun_to_adjective_ratio'])
        generate_histogram_plot_file(noun_to_adj_ratios, output_file_path)
    print('[[ DONE ]]')
