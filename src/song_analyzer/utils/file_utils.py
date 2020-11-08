import os


def create_dir_if_missing(dir_path: str):
    """
    Create directory path if doesn't exist
    :param dir_path: path to directory
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_lyrics_lines_from_song_file(path) -> list:
    """
    Get the lyrics from the song's file
    :return: the song's lyrics as lines
    """
    with open(path, 'r') as lyrics_file:
        return lyrics_file.readlines()
