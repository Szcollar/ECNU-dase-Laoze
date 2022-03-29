import os
import csv

baseDir = './data/csv/csv'

# print(1)

idiomDict = {}
bookDict = {}
authorDict = {}

with open(os.path.join(baseDir,'IDIOM.csv'),'r',encoding='utf-8') as csvFile:
    header = next(csvFile)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        idiomDict[row[0]] = row[1]

with open(os.path.join(baseDir,'BOOK.csv'),'r',encoding='utf-8') as csvFile:
    header = next(csvFile)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        bookDict[row[0]] = row[1]

with open(os.path.join(baseDir,'AUTHOR.csv'),'r',encoding='utf-8') as csvFile:
    header = next(csvFile)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        authorDict[row[0]] = row[1]

book_authorDict = {}
sub_bookDict = {}
idiom_bookDict = {}
sen_bookDict = {}
idiom_senDict = {}

with open(os.path.join(baseDir,'IDIOM_SEN.csv'),'r',encoding='utf-8') as csvFile:
    header = next(csvFile)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        idiom_senDict[row[0]] = row[1]

with open(os.path.join(baseDir,'BOOK_AUTH.csv'),'r',encoding='utf-8') as csvFile:
    header = next(csvFile)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        book_authorDict[row[0]] = row[1]

with open(os.path.join(baseDir,'SubBOOK_BOOK.csv'),'r',encoding='utf-8') as csvFile:
    header = next(csvFile)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        sub_bookDict[row[0]] = row[1]

with open(os.path.join(baseDir,'IDIOM_BOOK.csv'),'r',encoding='utf-8') as csvFile:
    header = next(csvFile)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        idiom_bookDict[row[0]] = row[2]

with open(os.path.join(baseDir,'SEN_BOOK.csv'),'r',encoding='utf-8') as csvFile:
    header = next(csvFile)
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        sen_bookDict[row[0]] = row[1]

dataDict = {}

for key,value in idiom_bookDict.items():
    flag = False
    while value[0] == 's':
        if sub_bookDict.get(value,'qweqwe')  == 'qweqwe':
            flag = True
            break
        if value == sub_bookDict[value]:
            flag = True
            break
        value = sub_bookDict[value]

    if flag == True:
        continue
    if book_authorDict.get(value,'qweqwe') == 'qweqwe':
        continue

    tempTuple = (bookDict[value],authorDict[book_authorDict[value]])
    dataDict[idiomDict[key]] = tempTuple

for key,value in idiom_senDict.items():
    flag = False

    if sen_bookDict.get(value,'qweqwe') == 'qweqwe':
        continue

    value = sen_bookDict[value]
    while value[0] == 's':
        if sub_bookDict.get(value,'qweqwe')  == 'qweqwe':
            flag = True
            break
        if value == sub_bookDict[value]:
            flag = True
            break
        value = sub_bookDict[value]
    if flag == True:
        continue
    if book_authorDict.get(value,'qweqwe') == 'qweqwe':
        continue

    tempTuple = (bookDict[value],authorDict[book_authorDict[value]])
    dataDict[idiomDict[key]] = tempTuple

def getData():
    dataList = []
    index = 0
    for key,value in dataDict.items():
        if len(value[1]) > 5:
            continue
        dataList.append((index,key,value[0],value[1]))
        index += 1
    return dataList

# dataList = getData()
# pass