from .sentence import Sentence


class Song:
    """ a Class representing a song's structure """

    def __init__(self, song_path: str):
        self.path = song_path
        self.lyrics = self.get_lyrics_from_song_file()
        # self.sentences = self.get_sentences()
        # self.metadata = self.get_song_metadata()

    def get_lyrics_from_song_file(self) -> str: # TODO - change the name of this function
        """
        Get the lyrics from the song's file
        :return: the song's lyrics
        """
        with open(self.path, 'r') as lyrics_file:
            return lyrics_file.read()

    def get_song_metadata(self) -> dict:
        """
        Extract the song's metadata, such as the artist's name and song's name
        :return: song's metadata
        """
        pass

    def get_sentences(self) -> list[Sentence]:
        """
        Get the song's 'Sentence' objects
        :return: the song's Sentence objects
        """
        pass

    def get_words_pos(self):
        """ Get each word's part of speech """
        pass

    def count_nouns(self) -> int:
        """
        Count the number of nouns in the song
        :return: number of nouns
        """
        pass

    def count_adjectives(self) -> int:
        """
        Count the number of adjectives in the song
        :return: number of adjectives
        """
        pass

    def get_nouns_to_adjectives_ratio(self) -> float:
        """
        Calculate the ratio between the number of nouns to the number of adjectives.
        :return: the ratio of nouns/adjectives
        """
        pass

    def get_sentence_length_stats(self) -> dict[str, int]:
        """
        Get statistics about the min/max/average length of the sentences in the song
        :return: sentences statistics
        """
        pass

    def get_word_length_stats(self) -> dict[str, int]:
        """
        Get statistics about the min/max/average length of the words in the song
        :return: words statistics
        """
        pass
