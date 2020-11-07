from textblob import TextBlob
import nltk


class Word:
    """ a Class representing a word's structure """

    def __init__(self, word_data: str):
        self.data = word_data.lower()
        self.pos = self.get_pos()

    def get_pos(self) -> str:
        """
        get the word's part of speech
        currently, there is no support for short words, such as "we'll" or "you've"
        :return: the word's POS, or an empty string if it's a shortened word
        """
        if "'" not in self.data:
            return TextBlob(self.data).tags[0][1]
        else:
            return ''
