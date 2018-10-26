from __future__ import division
import operator
import numpy as np
from functools import reduce

from naiveBayesClassifier.Exception import Notseen


class Classifier(object):

    def __init__(self, data_process, data_tokenizer):
        super(Classifier, self).__init__()
        self.data_process = data_process
        self.tokenizer = data_tokenizer
        self.defaultProb = 0.000000001

    def classify(self, text):
        
        documentCount = self.data_process.getDocNumber()
        classes = self.data_process.getClassNames()

        tokens = list(set(self.tokenizer.tokenize(text)))
        
        probsOfClasses = {}

        for className in classes:

            tokensProbs = [self.getTokenProb(token, className) for token in tokens]

            try:
                tokenSetProb = reduce(lambda a,b: np.log(a)+np.log(b) if a > 0 else a+np.log(b), (i for i in tokensProbs if i) )
            except:
                tokenSetProb = 0
            
            probsOfClasses[className] = tokenSetProb + np.log(self.getPrior(className))
        
        return sorted(probsOfClasses.items(), 
            key=operator.itemgetter(1), 
            reverse=True)


    def getPrior(self, className):

        return self.data_process.getClassDocNumber(className) / self.data_process.getDocNumber()

    def getTokenProb(self, token, className):

        classDocumentCount = self.data_process.getClassDocNumber(className)

        try:

            tokenFrequency = self.data_process.getTokenFrequencies(token, className)

        except Notseen as e:

            return None

        if tokenFrequency is None:

            return self.defaultProb

        probablity =  tokenFrequency / classDocumentCount

        return probablity
