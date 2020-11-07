import os
from song_analyzer.config import BASE_DIR, LYRICS_DIR, SCRIPT_OUTPUTS_DIR, CSV_COLUMNS
from song_analyzer.song_parts.song import Song
from song_analyzer.song_parts.artist import Artist
from song_analyzer.utils.utils import get_song_pos_entities, get_song_length_stats
import csv

if __name__ == '__main__':  # TODO - verbosity!!
    lyrics_dir = os.path.join(BASE_DIR, LYRICS_DIR)
    output_dir = os.path.join(BASE_DIR, SCRIPT_OUTPUTS_DIR)

    print('\n[ Getting all songs info.. ]\n')
    lyrics_files = [os.path.join(lyrics_dir, path) for path in os.listdir(lyrics_dir)]
    song_objects = [Song(lyrics) for lyrics in lyrics_files]

    artist_objects = {}
    for song_obj in song_objects:
        # Get Artist object
        artist_name = song_obj.metadata['artist']
        artist_output_dir = os.path.join(BASE_DIR, SCRIPT_OUTPUTS_DIR, artist_name)

        if not os.path.exists(artist_output_dir):
            os.makedirs(artist_output_dir)

        if artist_name not in artist_objects.keys():
            artist_objects[artist_name] = Artist(artist_name)
            # create general stats CSV file
            with open(os.path.join(artist_output_dir, 'general_statistics.csv'), 'w', newline='',
                      encoding='utf-8') as general_stats_file:
                writer = csv.DictWriter(general_stats_file, fieldnames=CSV_COLUMNS)
                writer.writeheader()

        artist_objects[artist_name].songs.append(song_obj)

        print('\n[[ {} ]]'.format(song_obj.metadata['name']))
        # Write POS entities to txt file
        print('[ writing POS entities ]')
        with open(os.path.join(artist_output_dir, 'pos_statistics.txt'), 'a') as pos_file:
            pos_entities = get_song_pos_entities(song_obj.path)
            pos_file.write('\n-- {} --\n'.format(song_obj.metadata['name']))
            pos_file.write('\n[ NOUNS ]\n')
            [pos_file.write(noun + '\n') for noun in set(pos_entities['nouns'])]
            pos_file.write('\n[ ADJECTIVES ]\n')
            [pos_file.write(adjective + '\n') for adjective in set(pos_entities['adjectives'])]
            pos_file.write('\nnoun/adjective ratio: {0} / {1} = {2}\n'.format(len(pos_entities['nouns']),
                                                                              len(pos_entities['adjectives']),
                                                                              pos_entities['noun_to_adjective_ratio']))
        # Write General stats to CSV
        print('[ writing general stats ]')
        with open(os.path.join(artist_output_dir, 'general_statistics.csv'), 'a', newline='',
                  encoding='utf-8') as general_stats_file:
            len_stats = get_song_length_stats(song_obj.path)
            writer = csv.DictWriter(general_stats_file, fieldnames=CSV_COLUMNS)
            writer.writerow(len_stats)

    # Create POS diagram for all artists
    print('\n[[ Create POS diagram for all artists ]]')
    [artist.get_noun_to_adj_ratio_hist_plot() for artist in artist_objects.values()]
    print('[[ DONE ]]')