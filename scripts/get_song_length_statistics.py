import sys
from song_analyzer.utils.utils import get_song_length_stats

if __name__ == '__main__':
    lyrics_path = sys.argv[1]
    len_stats = get_song_length_stats(lyrics_path)

    print('\n[ SENTENCE STATS ]\n')
    [print('{0}: {1}'.format(stat[0], stat[1])) for stat in len_stats['sentence_stats'].items()]

    print('\n[ WORDS STATS ]\n')
    [print('{0}: {1}'.format(stat[0], stat[1])) for stat in len_stats['word_stats'].items()]
