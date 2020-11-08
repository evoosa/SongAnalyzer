import sys

from song_analyzer.config import POS_STATS_FILENAME
from song_analyzer.song_parts.song import Song
from song_analyzer.utils.file_utils import update_pos_stats_file, print_file

if __name__ == '__main__':
    lyrics_path = sys.argv[1]
    song_obj = Song(lyrics_path)
    output_file = song_obj.metadata['name'] + '_' + POS_STATS_FILENAME
    update_pos_stats_file(output_file, song_obj)
    print_file(output_file)
