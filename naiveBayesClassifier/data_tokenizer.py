import re
from string import punctuation

class Data_tokenizer(object):

    def __init__(self, stop_words = ['and','or','with','up','on','of','the','a','an','in','out'], signs_to_remove = [punctuation]):

        self.stop_words = stop_words
        self.signs_to_remove = signs_to_remove

    def tokenize(self,text):

        return text.lower().split(' ')

    def remove_stop_words(self,token):

        if token in self.stop_words:
            return ""

        else:
            return token

    def remove_punctuation(self,token):

        return re.sub(str(self.signs_to_remove),"",token)