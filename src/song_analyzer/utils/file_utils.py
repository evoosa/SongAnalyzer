def get_lyrics_from_song_file(path) -> list:
    """
    Get the lyrics from the song's file
    :return: the song's lyrics
    """
    with open(path, 'r') as lyrics_file:
        return lyrics_file.readlines()