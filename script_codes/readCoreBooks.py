import os
import re

subDynasty = re.compile('\((.*?)\)',re.S)
findDynasty = re.compile('\((.*?)\)',re.S)

bookIdDict = {}
subIdDict = {}
bookDataList = []

bookCurrent = 0
subCurrent = 0

baseInstroDir = './data/BookIntro'
baseBookDir = './data/books'

instroSecList = os.listdir(baseInstroDir)
for instroSec in instroSecList:
    for instro in os.listdir(os.path.join(baseInstroDir,instroSec)):
        bookName = re.sub(subDynasty,'',instro)[0:-4]
        dynastyName = re.findall(findDynasty,instro)[0]
        with open(os.path.join(os.path.join(baseInstroDir,instroSec),instro),'r',encoding='utf-8') as txtFile:
            bookIdDict[bookName] = 'book'+str(bookCurrent)
            bookDataList.append((bookIdDict[bookName],bookName,instroSec,dynastyName,txtFile.read()))
            bookCurrent += 1

contentList = []
relationDict = {}

def getCotent(path):
    with open(path,'r',encoding='utf-8') as file:
        return file.read()

# print(getCotent('./sdfsdfsdf.txt'))

def judgeDepth(path):
    if not os.path.isdir(os.path.join(path,os.listdir(path)[0])):
        return 1
    else:
        return 1 + judgeDepth(os.path.join(path,os.listdir(path)[0]))


bookList = os.listdir(baseBookDir)
for book in bookList:
    translationFlag = 0
    bookPath = os.path.join(baseBookDir,book)
    if judgeDepth(bookPath) == 2:

        subIdDict['subook' + str(subCurrent)] = '全部'
        if bookIdDict.get(book, 'qweqwe') == 'qweqwe':
            bookIdDict[book] = 'book' + str(bookCurrent)
            bookCurrent += 1
            bookDataList.append((bookIdDict[book], book,'', '', ''))
        relationDict['subook' + str(subCurrent)] = bookIdDict[book]


        for chapter in os.listdir(bookPath):
            content = ''
            translation = ''
            chapterPath = os.path.join(bookPath,chapter)
            if len(os.listdir(chapterPath)) == 2:
                translationFlag = 1
            else:
                translationFlag = 0

            content = getCotent(os.path.join(chapterPath,'原文.txt'))
            if translation == 1:
                translationFlag = getCotent(os.path.join(chapterPath,'译文.txt'))
            contentList.append(('subook'+str(subCurrent),'全部',chapter,translationFlag,content,translation))
        subCurrent += 1

    # translationFlag = 0
    # bookPath = os.path.join(baseBookDir,book)
    # if judgeDepth(bookPath) == 2:
    #     for chapter in os.listdir(bookPath):
    #         content = ''
    #         translation = ''
    #         chapterPath = os.path.join(bookPath,chapter)
    #         if len(os.listdir(chapterPath)) == 2:
    #             translationFlag = 1
    #         else:
    #             translationFlag = 0
    #         subIdDict['subook'+str(subCurrent)] = chapter
    #
    #         if bookIdDict.get(book,'qweqwe') == 'qweqwe':
    #             bookIdDict[book] = 'book' + str(bookCurrent)
    #             bookCurrent += 1
    #             bookDataList.append((bookIdDict[book],book,'',''))
    #
    #         relationDict['subook'+str(subCurrent)] = bookIdDict[book]
    #         content = getCotent(os.path.join(chapterPath,'原文.txt'))
    #         if translation == 1:
    #             translationFlag = getCotent(os.path.join(chapterPath,'译文.txt'))
    #         contentList.append(('subook'+str(subCurrent),chapter,'全部',translationFlag,content,translation))
    #         subCurrent += 1
    else:
        for chapter in os.listdir(bookPath):

            subIdDict['subook' + str(subCurrent)] = chapter

            if bookIdDict.get(book, 'qweqwe') == 'qweqwe':
                bookIdDict[book] = 'book' + str(bookCurrent)
                bookCurrent += 1
                bookDataList.append((bookIdDict[book], book, '','', ''))
            relationDict['subook' + str(subCurrent)] = bookIdDict[book]
            chapterPath = os.path.join(bookPath,chapter)

            for subChapter in os.listdir(chapterPath):
                subChapterPath = os.path.join(chapterPath,subChapter)
                if len(os.listdir(subChapterPath)) == 2:
                    translationFlag = 1
                else:
                    translationFlag = 0
                content = getCotent(os.path.join(subChapterPath,'原文.txt'))
                translation = ''
                if translationFlag == 1:
                    translation = getCotent(os.path.join(subChapterPath,'译文.txt'))
                contentList.append(('subook'+str(subCurrent),chapter,subChapter,translationFlag,content,translation))
            subCurrent += 1

pass