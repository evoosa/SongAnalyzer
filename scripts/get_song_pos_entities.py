import sys
from song_analyzer.utils.song_analysis_utils import get_pos_entities_from_sentences
from song_analyzer.song_parts.song import Song

if __name__ == '__main__':
    lyrics_path = sys.argv[1]
    song_obj = Song(lyrics_path)
    song_pos_entities = get_pos_entities_from_sentences(song_obj.sentences)
    print('\n[ NOUNS ]\n')
    [print(noun) for noun in set(song_pos_entities['nouns'])]

    print('\n[ ADJECTIVES ]\n')
    [print(adjective) for adjective in set(song_pos_entities['adjectives'])]

    print('\nnoun/adjective ratio: {0} / {1} = {2}\n'.format(len(song_pos_entities['nouns']),
                                                             len(song_pos_entities['adjectives']),
                                                             song_pos_entities['noun_to_adjective_ratio']))
