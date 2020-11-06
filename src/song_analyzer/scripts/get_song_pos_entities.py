from song_analyzer.song_parts.song import Song
from song_analyzer.utils import get_words_with_pos_tags

if __name__ == '__main__':
    song_path = r"C:\Users\evoosa\Desktop\JobShit\SongAnalyzer\lyrics\charlie_cunningham-force_of_habit.txt"
    song_obj = Song(song_path)
    song_obj.get_words_pos()

    # print all Nouns and Adjectives in the song
    nouns = get_words_with_pos_tags(song_obj, ['NN', 'NNS', 'NNP', 'NNPS'])
    adjectives = get_words_with_pos_tags(song_obj, ['JJ', 'JJR', 'JJS'])

    print('\n[ NOUNS ]\n')
    [print(noun) for noun in nouns]

    print('\n[ ADJECTIVES ]\n')
    [print(adjective) for adjective in adjectives]

    # calculate the ratio between the nouns and adjectives
    print('\nnoun/adjective ratio: {}\n'.format(len(nouns) / len(adjectives)))
