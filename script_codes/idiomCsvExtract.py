import os
import csv
import random
from urllib.parse import quote, unquote
from getFromBaidu import getData
import re
from jaccard import jaccard

csvPath="./data/idiom.csv"
explainPath = "./explain.txt"
idiomList = []
findExplain = re.compile(r'。(.*?)。',re.S)

def writeInTxt(dataList):
    with open(explainPath,'w',encoding='utf-8') as txtFile:
        for List in dataList:
            for row in List:
                txtFile.write(row+'\n')
            txtFile.write('\n')

def extractIdiom():
    with open(csvPath,'r',encoding = 'utf-8') as csvFile:
        readFile = csv.reader(csvFile)
        next(readFile)
        for row in readFile:
            # print(row)
            # break
            if row[4] != ' ' and row[5] != ' ' and row[8] != ' ':
                idiomList.append(row)

    random.shuffle(idiomList)
    random.shuffle(idiomList)


writeList = []


def iteratorIdiom(num):
    index = 0
    current = 0
    sumSimility = 0
    while True:
        idiom = idiomList[current][0]
        idiomExplain = idiomList[current][3]
        if re.findall(findExplain,idiomExplain) != []:
            idiomExplain = re.findall(findExplain,idiomExplain)[0]
        current += 1
        url = 'https://baike.baidu.com/item/'+idiom
        url = quote(url, safe=";/?:@&=+$,", encoding="utf-8")
        baiduExplain,flag = getData(url)
        if flag == 0:
            continue
        if baiduExplain == []:
            continue

        simility = jaccard(idiomExplain,baiduExplain[0])
        sumSimility += simility

        temp = [idiom,idiomExplain,baiduExplain[0],flag,str(simility)]
        writeList.append(temp)
        writeInTxt(writeList)
        index += 1
        print(str(index)+'   '+str(simility))

        if index == num:
            print(sumSimility/num)
            break

extractIdiom()
iteratorIdiom(50)




# for i in range(0,20):
#     print(idiomList[i][0]+'\t'+idiomList[i][3])

