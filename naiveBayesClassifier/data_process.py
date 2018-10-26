import sys
from naiveBayesClassifier.Exception import Notseen
from naiveBayesClassifier.data_tokenizer import Data_tokenizer


class Data_process(object):
    def __init__(self):
        self.docNumberOfClasses = {}
        self.tokenFrequencies = {}
        self.tokenizer = Data_tokenizer()

    def increaseDocNumberOfClasses(self, className):
        self.docNumberOfClasses[className] = self.docNumberOfClasses.get(className, 0) + 1

    def increaseTokenFrequencies(self, token, className):

        if not token in self.tokenFrequencies:
                self.tokenFrequencies[token] = {}

        self.tokenFrequencies[token][className] = self.tokenFrequencies[token].get(className, 0) + 1

    def decreaseTokenFrequencies(self, token, className, byAmount=1):

        if token not in self.tokenFrequencies:
            raise Notseen(token)

        tokenClassNumber = self.tokenFrequencies[token]

        if className not in self.tokenFrequencies:

            sys.stderr.write("Warning: token %s has no entry for class %s. Not decreasing.\n" % (token, className))
            return

        if tokenClassNumber[className] < byAmount:
            raise ArithmeticError("Could not decrease %s/%s count (%i) by %i, "
                                  "as that would result in a negative number." % (
                                      token, className, tokenClassNumber[className], byAmount))

        tokenClassNumber[className] -= byAmount

    def getDocNumber(self):

        return sum(self.docNumberOfClasses.values())

    def getClassNames(self):

        return self.docNumberOfClasses.keys()

    def getClassDocNumber(self, className):

        return self.docNumberOfClasses.get(className, None)

    def getTokenFrequencies(self, token, className):

        if token in self.tokenFrequencies:

            tokenClassNumber = self.tokenFrequencies[token]

            return tokenClassNumber.get(className)

        else:
            raise Notseen(token)

    def final_process(self,text, className):

        self.increaseDocNumberOfClasses(className)

        tokens = self.tokenizer.tokenize(text)

        for token in tokens:
            token = self.tokenizer.remove_stop_words(token)
            token = self.tokenizer.remove_punctuation(token)
            self.increaseTokenFrequencies(token, className)
