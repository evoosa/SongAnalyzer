from song_analyzer.song_parts.song import Song
from song_analyzer.utils import get_sentence_length_stats, get_word_length_stats

if __name__ == '__main__':
    song_path = r"C:\Users\evoosa\Desktop\JobShit\SongAnalyzer\lyrics\charlie_cunningham-force_of_habit.txt"
    song_obj = Song(song_path)

    # print the sentences statistics
    sentence_stats = get_sentence_length_stats(song_obj)
    print('\n[ SENTENCE STATS ]\n')
    [print('{0}: {1}'.format(stat[0], stat[1])) for stat in sentence_stats.items()]

    # print the words statistics
    words_stats = get_word_length_stats(song_obj)
    print('\n[ WORDS STATS ]\n')
    [print('{0}: {1}'.format(stat[0], stat[1])) for stat in words_stats.items()]