import sys,os
import random, shutil

def getDirlist(path):

    dirs=os.listdir(path)
    file_list=[]

    for file in dirs:
        if file != '.DS_Store':
            file_list.append(file)

    return file_list

def createDir(dirlist):

    os.system('mkdir train_data')

    for dir in dirlist:
        os.system('mkdir train_data/'+dir)

def partition(dirList):

    for dir in dirList:
        pathDir='./20_newsgroups/'+dir+'/'
        sample=random.sample(os.listdir(pathDir), 500)

        for name in sample:
            os.system('mv '+pathDir+name+' ./train_data/'+dir+'/'+name)

if __name__ == '__main__':

    path='./20_newsgroups/'
    allDirList=getDirlist(path)
    createDir(allDirList)
    partition(allDirList)
    os.system('mv 20_newsgroups/ test_data')
