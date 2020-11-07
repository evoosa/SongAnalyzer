from .sentence import Sentence
import ntpath
import os


class Song:
    """ a Class representing a song's structure """

    def __init__(self, song_path: str):
        self.path = song_path
        self.lyrics = self.get_lyrics_from_song_file()
        self.metadata = self.get_song_metadata()
        self.sentences = self.get_sentences()
        self.nouns = self.get_words_with_pos_tags(['NN', 'NNS', 'NNP', 'NNPS'])
        self.adjectives = self.get_words_with_pos_tags(['JJ', 'JJR', 'JJS'])
        self.noun_to_adj_ratio = len(self.nouns) / len(self.adjectives)

    def get_lyrics_from_song_file(self) -> list: # TODO - change the name of this function
        """
        Get the lyrics from the song's file
        :return: the song's lyrics
        """
        with open(self.path, 'r') as lyrics_file:
            return lyrics_file.readlines()

    def get_song_metadata(self) -> dict:
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
        :return: the song's Sentence objects
        """
        sentences = []
        for sentence in self.lyrics:
            sentence_obj = Sentence(sentence.replace('\n', ''))
            sentences.append(sentence_obj)
        return sentences

    def get_words_with_pos_tags(self, pos_tags: list) -> list:
        """
        Get words with on of the given POS tags
        :param self: Song object
        :param pos_tags: POS tags to search songs with
        :return:
        """
        words = []
        for sentence in self.sentences:
            for word in sentence.words:
                if word.pos in pos_tags:
                    words.append(word.data)
        return words