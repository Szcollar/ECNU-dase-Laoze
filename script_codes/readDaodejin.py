import os

baseDir = './data/道德经'
chapterDirList = os.listdir(baseDir)
nameList = ['context.txt', 'note.txt', 'translation.txt']

def returnClass(string):
    if string == 'context.txt':
        return '原文'
    elif string == 'note.txt':
        return '注释'
    else:
        return '译文'

def returnSection(index):
    if index < 38:
        return '道'
    else:
        return '德'

def getDaoDeJinSql():
    dataList = []
    index = 0

    for chapter in chapterDirList:
        temp = []
        temp.append(chapter[1:-1])
        for content in nameList:
            filePath = os.path.join(os.path.join(baseDir,chapter),content)
            with open(filePath,'r',encoding='utf-8') as txtFile:
                temp.append(txtFile.read())
                # temp = (int(index),txtFile.read(),returnClass(content),chapter,returnSection(int(chapter[1:-1])))
        dataList.append((temp[0],temp[1],temp[3],temp[2]))

    return dataList

# print(getDaoDeJinSql())
# string = 'sdf'
# print(string[0:2])