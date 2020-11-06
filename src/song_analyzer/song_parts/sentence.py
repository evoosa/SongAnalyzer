from .word import Word


class Sentence:
    """ a Class represnting a sentence's structure """

    def __init__(self, sentence_data: str):
        self.data = sentence_data
        self.words = self.get_words_from_data()

    def get_words_from_data(self) -> list[Word]:
        """
        Get the 'Word' objects from the given sentence data
        :return: Word objects
        """
        words = []
        for word in self.data.split(' '):
            word_obj = Word(word)
            words.append(word_obj)
        return words
