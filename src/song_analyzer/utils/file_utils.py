def get_lyrics_lines_from_song_file(path) -> list:
    """
    Get the lyrics from the song's file
    :return: the song's lyrics as lines
    """
    with open(path, 'r') as lyrics_file:
        return lyrics_file.readlines()