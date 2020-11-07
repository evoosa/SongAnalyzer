from song_analyzer.song_parts.song import Song

if __name__ == '__main__':
    song_path = r"C:\Users\User\Desktop\PS\SongAnalyzer\lyrics\charlie_cunningham-dont_go_far.txt"
    song_obj = Song(song_path)

    # print all Nouns and Adjectives in the song

    print('\n[ NOUNS ]\n')
    [print(noun) for noun in song_obj.nouns]

    print('\n[ ADJECTIVES ]\n')
    [print(adjective) for adjective in song_obj.adjectives]

    # calculate the ratio between the nouns and adjectives
    print('\nnoun/adjective ratio: {0} / {1} = {2}\n'.format(len(song_obj.nouns), len(song_obj.adjectives), song_obj.noun_to_adj_ratio))
