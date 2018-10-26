import os,sys,re
from naiveBayesClassifier.data_process import Data_process
from naiveBayesClassifier.classifier import Classifier

def get_train_data(path_train):

    newsData_train=[]
    classList_train = []
    for file in os.listdir(path_train):
        if file != '.DS_Store':
            classList_train.append(file)
    print(len(classList_train))
    print(classList_train)
    for i in range(len(classList_train)):

        newsList_train = os.listdir('train_data/' + classList_train[i] + '/')

        for j in range(len(newsList_train)):
            with open('train_data/' + classList_train[i] + '/' + newsList_train[j], 'rb') as file:
                document_train = file.read()
                # print('class: ',classList[i])
                # print('document: ',newsList[j])
                documentText_train = str(document_train).replace('\n', ' ')

            documentDic_train = {}
            documentDic_train['text'] = documentText_train
            documentDic_train['category'] = classList_train[i]
            newsData_train.append(documentDic_train)

    return newsData_train

def get_test_data(path_test):

    newsData_test=[]
    classList_test = []
    for file in os.listdir(path_test):
        if file != '.DS_Store':
            classList_test.append(file)

    print(len(classList_test))
    print(classList_test)

    for i in range(len(classList_test)):
        newsList_test = os.listdir('test_data/' + classList_test[i] + '/')

        for j in range(len(newsList_test)):
            with open('test_data/' + classList_test[i] + '/' + newsList_test[j], 'rb') as file_test:
                document_test = file_test.read()
                documentText_test = str(document_test).replace('\n', ' ')

            documentDic_test = {}
            documentDic_test['text'] = documentText_test
            documentDic_test['category'] = classList_test[i]
            newsData_test.append(documentDic_test)

    return newsData_test

def train_classifier(newsData_train):

    data_process = Data_process()

    for data in newsData_train:
        data_process.final_process(data['text'], data['category'])

    newsClassifier = Classifier(data_process, data_process.tokenizer)

    return newsClassifier

def classify_test_data(newsData_test, newsClassifier):

    count = 0

    for item in newsData_test:
        classification = newsClassifier.classify(item['text'])

        if classification[0][0] == item['category']:
            count += 1

    precision = count / 10000

    return precision


if __name__=='__main__':

    path_train = 'train_data/'
    newsData_train = get_train_data(path_train)

    path_test = 'test_data/'
    newsData_test = get_test_data(path_test)

    newsClassifier=train_classifier(newsData_train)

    test_precision=classify_test_data(newsData_test, newsClassifier)

    print('Classification precision is ', test_precision)