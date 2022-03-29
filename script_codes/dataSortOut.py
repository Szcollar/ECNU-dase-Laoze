import os

ancientPath = './data/ancient_chinese_books/首页'
booksPath = './data/books'
# ancientPath = r'C:\Users\lenovo\Desktop\data_project\data\ancient_chinese_books\首页\集藏\谜语'

def getBooksNum(path):
    num = 0
    pathList = os.listdir(path)
    if len(pathList) == 0:
        return 0
    if os.path.isdir(os.path.join(path,pathList[0])):
        for dirName in pathList:
            num += getBooksNum(os.path.join(path,dirName))
        return num
    else:
        return len(pathList)

def getTranslationNum(path):
    num = 0
    pathList = os.listdir(path)
    if len(pathList) == 0:
        return 0
    if os.path.isdir(os.path.join(path,pathList[0])):
        for dirName in pathList:
            num += getTranslationNum(os.path.join(path,dirName))
        return num
    else:
        return len(pathList)-1

# print(getBooksNum(ancientPath))
# print(getTranslationNum(ancientPath))
#
# print(getBooksNum(booksPath))
# print(getTranslationNum(booksPath))

def getAuthorNum(authorPath):
    dataList = os.listdir(authorPath)
    num = 0
    for dynasty in dataList:
        path = os.path.join(authorPath,dynasty)
        if not os.path.isdir(path):
            continue
        num += len(os.listdir(path))
    return num

print(getAuthorNum('./data/author'))