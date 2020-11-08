class Sentence:
    """ a Class represnting a sentence's structure """

    def __init__(self, sentence_data: str):
        self.data = sentence_data
        self.words = [word.lower() for word in self.data.split(' ')]
