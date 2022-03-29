import os

baseDir = './data/author'

txtFileName = 'introduce.txt'

def getIntro(path):
    with open(path,'r',encoding='utf-8') as txtFile:
        return txtFile.read()

# print(bytes('txtFile.read()', 'utf-8').decode('utf-8', 'ignore'))


def getData():
    index = 0
    dataList = []
    dynastyList = os.listdir(baseDir)
    for dynasty in dynastyList:
        dynastyDir = os.path.join(baseDir,dynasty)
        authorList = os.listdir(dynastyDir)
        for author in authorList:
            authorPath = os.path.join(dynastyDir,author)
            imgPath = ''
            if len(os.listdir(authorPath)) == 2:
                imgPath = os.path.join(authorPath, os.listdir(authorPath)[1])
            else:
                imgPath = ' '
            tempTuple = (str(index),author,dynasty,getIntro(os.path.join(authorPath,txtFileName)),imgPath)
            index += 1
            dataList.append(tempTuple)
    return dataList


