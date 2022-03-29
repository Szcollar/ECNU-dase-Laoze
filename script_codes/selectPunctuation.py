import os

inCoreDir = './data/ancient_chinese_books'
coreDir = './data/books'

def getBookPathList(dirPath,ansList):
    if not os.path.isdir(dirPath):
        ansList.append(dirPath)
        return
    fileList = os.listdir(dirPath)
    for file in fileList:
        if file == '译文.txt':
            continue
        getBookPathList(os.path.join(dirPath,file),ansList)

coreList = []
inCoreList = []

getBookPathList(inCoreDir,inCoreList)
getBookPathList(coreDir,coreList)