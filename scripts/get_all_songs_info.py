#!/usr/bin/python3
import os

from song_analyzer.config import SCRIPT_OUTPUTS_DIR, HISTOGRAM_PLOT_FILENAME, LYRICS_FILE_PATHS, GEN_STATS_FILENAME, \
    POS_STATS_FILENAME
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.file_utils import create_dir_if_missing, create_gen_stats_csv, update_pos_stats_file, \
    update_gen_stats_file
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
            create_gen_stats_csv(os.path.join(artist_output_dir, GEN_STATS_FILENAME))
        artists[artist_name]['songs'].append(song_obj)

        print('\n[[ {} ]]'.format(song_obj.metadata['name']))
        print('[ updating POS entities ]')
        update_pos_stats_file(os.path.join(artist_output_dir, POS_STATS_FILENAME), song_obj)
        print('[ updating general stats ]')
        update_gen_stats_file(os.path.join(artist_output_dir, GEN_STATS_FILENAME), song_obj)

    print('\n[[ Create POS histograms for all artists ]]')
    for artist in artists.values():
        plot_file_path = os.path.join(artist['output_dir'], HISTOGRAM_PLOT_FILENAME)
        gen_hist_plot_from_songs(plot_file_path, artist['songs'])
    print('[[ DONE ]]')
