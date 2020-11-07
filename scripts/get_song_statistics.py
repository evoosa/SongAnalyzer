from song_analyzer.song_parts.song import Song
from song_analyzer.utils.song_utils import get_sentence_length_stats, get_word_length_stats
import sys

if __name__ == '__main__':
    lyrics_path = sys.argv[1]
    song_obj = Song(lyrics_path)

    # print the sentences statistics
    sentence_stats = get_sentence_length_stats(song_obj)
    print('\n[ SENTENCE STATS ]\n')
    [print('{0}: {1}'.format(stat[0], stat[1])) for stat in sentence_stats.items()]

    # print the words statistics
    words_stats = get_word_length_stats(song_obj)
    print('\n[ WORDS STATS ]\n')
    [print('{0}: {1}'.format(stat[0], stat[1])) for stat in words_stats.items()]
