from askurl import askURL
from bs4 import BeautifulSoup
import re
import os

find = re.compile(r'<p class="STYLE4">(.*?)</p>',re.S)
findContent = re.compile(r'[原文] </p>, <p class="STYLE4">(.*?)</p>',re.S)
findTranslation = re.compile(r'<p class="STYLE4">[译文] </p>, <p class="STYLE4">(.*?)</p>',re.S)
findNote = re.compile(r'[注释] </p>, <p class="STYLE4">(.*?)<p class="STYLE4 STYLE5">',re.S)

translation = '[译文] '
note = '[注释] '

baseUrl = 'https://www.daodejing.org/'

basePath = './data/道德经1'

if not os.path.exists(basePath):
    os.mkdir(basePath)

def concatUrl(index):
    return baseUrl+'/'+str(index)+'.html'

def getSoup(index):
    soup = BeautifulSoup(askURL(concatUrl(index)), 'html.parser')
    soup = str(soup.find_all('p',class_ = 'STYLE4'))
    return soup

def getOneSoupList(soup):
    dataList = re.findall(find,soup)
    return dataList

def getNote(dataList,index):
    noteList = []
    while True:
        if dataList[index].find('<p class=\"STYLE4\">') != -1:
            temp = dataList[index].replace('<p class="STYLE4">', '')
            temp = temp.replace('\u3000','')
            temp = temp.replace(' ','')
            noteList.append(temp)
            break
        noteList.append(dataList[index])
        index += 1
    return noteList

def getDataFromOneSoup(dataList):
    context = None
    translate = None
    noteList = None
    for i in range(len(dataList)):
        if dataList[i] == translation:
            context = dataList[i-1]
            translate = dataList[i+1]
        if dataList[i] == note:
            noteList = getNote(dataList,i+1)
    return context,translate,noteList

def writeInTxt(index,context,translate,noteList):
    path = os.path.join(basePath,'第'+str(index)+'章')
    if not os.path.exists(path):
        os.mkdir(path)
    contextTxt = os.path.join(path,'context.txt')
    translationTxt = os.path.join(path,'translation.txt')
    noteTxt = os.path.join(path,'note.txt')

    with open(contextTxt,'w',encoding='utf-8') as textFile:
        textFile.write(context)
    with open(translationTxt, 'w', encoding='utf-8') as textFile:
        textFile.write(translate)
    with open(noteTxt,'w',encoding='utf-8') as textFile:
        for row in noteList:
            textFile.write(row+'\n')


if __name__ == '__main__':
    # error = []
    # for i in range(1,82):
    #     context,translate,noteList = getDataFromOneSoup(getOneSoupList(getSoup(i)))
    #     if context == None or translate == None or noteList == None:
    #         error.append(i)
    #         continue
    #     writeInTxt(i,context,translate,noteList)
    # for i in error:
    #     print(i)

    # dirList = os.listdir(basePath)
    # for dir in dirList:
    #     path = os.path.join(os.path.join(basePath,dir),'translation.txt')
    #     with open(path,'r',encoding='utf-8') as txtFile:
    #         print(os.path.split(path)[-2],'      ',txtFile.read())
    #         print('**********************************')






