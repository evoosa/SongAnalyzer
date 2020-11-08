#!/usr/bin/python3
import sys
import os

from song_analyzer.config import POS_STATS_FILENAME, SCRIPT_OUTPUTS_DIR
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.file_utils import update_pos_stats_file, print_file, create_dir_if_missing

if __name__ == '__main__':
    lyrics_path = sys.argv[1]
    song_obj = Song(lyrics_path)
    output_file = os.path.join(SCRIPT_OUTPUTS_DIR, song_obj.metadata['name'] + '_' + POS_STATS_FILENAME)
    create_dir_if_missing(SCRIPT_OUTPUTS_DIR)
    update_pos_stats_file(output_file, song_obj)
    print_file(output_file)
    print('File location: {}'.format(output_file))
