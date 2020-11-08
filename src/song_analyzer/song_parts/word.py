from textblob import TextBlob

class Word:
    """ a Class representing a word's structure """

    def __init__(self, word_data: str):
        self.data = word_data
        self.pos = self.get_pos()


