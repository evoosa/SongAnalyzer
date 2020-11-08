import os

from song_analyzer.config import SCRIPT_OUTPUTS_DIR, HISTOGRAM_PLOT_FILENAME, LYRICS_FILE_PATHS
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.file_utils import create_dir_if_missing, create_gen_stats_csv, update_pos_stats_file, \
    update_general_stats_file
from song_analyzer.utils.histogram_utils import gen_hist_plot_from_songs

if __name__ == '__main__':

    print('\n[ Getting all songs info.. ]\n')
    song_objects = [Song(lyrics) for lyrics in LYRICS_FILE_PATHS]
    artists = {}
    for song_obj in song_objects:
        artist_name = song_obj.metadata['artist']
        artist_output_dir = os.path.join(SCRIPT_OUTPUTS_DIR, artist_name)
        create_dir_if_missing(artist_output_dir)

        if artist_name not in artists.keys():
            artists[artist_name] = dict(songs=[], output_dir=artist_output_dir)
            create_gen_stats_csv(os.path.join(artist_output_dir, 'general_statistics.csv'))

        artists[artist_name]['songs'].append(song_obj)
        print('\n[[ {} ]]'.format(song_obj.metadata['name']))
        print('[ updating POS entities ]')
        update_pos_stats_file(os.path.join(artist_output_dir, 'pos_statistics.txt'), song_obj)
        print('[ updating general stats ]')
        update_general_stats_file(os.path.join(artist_output_dir, 'general_statistics.csv'), song_obj)

    print('\n[[ Create POS histograms for all artists ]]')
    for artist in artists.values():
        gen_hist_plot_from_songs(os.path.join(artist['output_dir'], HISTOGRAM_PLOT_FILENAME), artist['songs'])
    print('[[ DONE ]]')
