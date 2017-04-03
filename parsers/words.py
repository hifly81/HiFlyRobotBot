import re


class WordsMatcher:

    def __init__(self):
        pass

    def find_greeting(self, phrase, greets):
        for key in greets.iterkeys():
            if self.find_word(key)(phrase) is not None:
                return key
        return None

    def find_word(self, word):
        """Match the exact word in phrase
        """
        return re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE).search


