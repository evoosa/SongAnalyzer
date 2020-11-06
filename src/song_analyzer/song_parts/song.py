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

    def get_lyrics_from_song_file(self) -> str: # TODO - change the name of this function
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

    def get_words_pos(self):
        """ Get the part of speech for all the words in the song """
        for sentence in self.sentences:
            for word in sentence.words:
                word.get_pos()

    def __count_words_with_pos_tags(self, pos_tags: list) -> int:
        """
        Count the number of words in the song with one of the given POS tags
        :return: number of words with POS tags
        """
        count = 0
        for sentence in self.sentences:
            for word in sentence.words:
                if word.pos in pos_tags:
                    count += 1
        return count

    def get_nouns_to_adjectives_ratio(self) -> float:
        """
        Calculate the ratio between the number of nouns to the number of adjectives.
        :return: the ratio of nouns/adjectives
        """
        nouns_count = self.__count_words_with_pos_tags(['NN', 'NNS', 'NNP', 'NNPS'])
        adjective_count = self.__count_words_with_pos_tags(['JJ', 'JJR', 'JJS'])
        return nouns_count/adjective_count # FIXME - should i leagel???????????????????????????????????????????????????????????

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
