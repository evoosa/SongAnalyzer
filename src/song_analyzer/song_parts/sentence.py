from .word import Word


class Sentence:
    """ a Class represnting a sentence's structure """

    def __init__(self, sentence_data: str):
        self.data = sentence_data
        # words = self.get_words_from_data()

    def get_words_from_data(self) -> list[Word]:
        """
        Get the 'Word' objects from the given sentence data
        :return: Word objects
        """
        pass
