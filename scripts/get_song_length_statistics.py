import sys
from song_analyzer.utils.song_analysis_utils import get_song_length_stats
from song_analyzer.song_parts.song import Song

if __name__ == '__main__':
    lyrics_path = sys.argv[1]
    song_obj = Song(lyrics_path)
    len_stats = get_song_length_stats(song_obj.sentences)

    print('\n[ LENGTH STATS ]\n')
    [print('{0}: {1}'.format(stat[0], stat[1])) for stat in len_stats.items()]