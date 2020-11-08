import ntpath
import os

from song_analyzer.utils.file_utils import get_lyrics_from_song_file
from song_analyzer.song_parts.sentence import Sentence


class Song:
    """ a Class representing a song's structure """

    def __init__(self, song_path: str):
        self.path = song_path
        self.lyrics = get_lyrics_from_song_file(self.path)
        self.metadata = self.get_metadata()
        self.sentences = self.get_sentences()

    def get_metadata(self) -> dict:
        """
        Extract the song's metadata from it's filename,
        such as the artist's name and song's name
        :return: song's metadata
        """
        filename = os.path.splitext(ntpath.basename(self.path))[0]
        filename_splitted = filename.split('-')
        return dict(name=filename_splitted[1], artist=filename_splitted[0])

    def get_sentences(self) -> list[Sentence]:
        """
        Get the song's 'Sentence' objects
        Remove ',' character from words
        :return: the song's Sentence objects
        """
        sentences = []
        for sentence in self.lyrics:
            sentence_obj = Sentence(sentence.replace('\n', '').replace(',', ''))
            sentences.append(sentence_obj)
        return sentences
