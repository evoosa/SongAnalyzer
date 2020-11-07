from textblob import TextBlob
import nltk


class Word:
    """ a Class representing a word's structure """

    def __init__(self, word_data: str):
        self.data = word_data.lower()
        self.pos = self.get_pos()

    def get_pos(self):
        """
        get the word's part of speech
        """
        return TextBlob(self.data).tags[0][1]
