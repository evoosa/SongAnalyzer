from song_analyzer.song_parts.song import Song
import sys

if __name__ == '__main__':
    lyrics_path = sys.argv[1]
    song_obj = Song(lyrics_path)

    # print all Nouns and Adjectives in the song

    print('\n[ NOUNS ]\n')
    [print(noun) for noun in song_obj.nouns]

    print('\n[ ADJECTIVES ]\n')
    [print(adjective) for adjective in song_obj.adjectives]

    # calculate the ratio between the nouns and adjectives
    print('\nnoun/adjective ratio: {0} / {1} = {2}\n'.format(len(song_obj.nouns), len(song_obj.adjectives), song_obj.noun_to_adj_ratio))
