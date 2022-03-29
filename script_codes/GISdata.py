import os
import re

sub = re.compile('（(.*?)）')

baseDir = './data/GISdata'
stanfordDir = './data/GISner/stanfordcorenlp'
pyhanlpDir = './data/GISner/pyhanlp'
instroDir = './data/baiduInstro'

stanfordBookTxtList = os.listdir(stanfordDir)
pyhanlpBookTxtList = os.listdir(pyhanlpDir)

def isChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def isTwo(string):
    if content[tmp - 3] == '家' or content[tmp - 3] == '期' or isChinese(content[tmp - 3]) == False or content[tmp - 3] == '元' or content[tmp - 3] == '明' or content[tmp - 3] == '清' or content[tmp - 3] == '，' or content[tmp - 3] == '是' or content[tmp - 3] == '代' or content[tmp - 3] == '朝':
        return True
    else:
        return False

bookDict = {}
dynasty = ('元','明','清')
for bookTxt in stanfordBookTxtList:
    with open(os.path.join(instroDir,bookTxt),'r',encoding='utf-8') as txtFile:
        content = re.sub(sub,'',txtFile.read())
        tmp = content.find('所著')
        if tmp != -1:
            i = 3
            if isTwo(content[tmp-3]):
                i = 2
            bookDict[bookTxt[0:-4]] = [content[tmp - i:tmp]]
            continue
        tmp = content.find('修撰')
        if tmp != -1:
            i = 3
            if isTwo(content[tmp-3]):
                i = 2
            bookDict[bookTxt[0:-4]] = [content[tmp-i:tmp]]
            continue
        tmp = content.find('撰')
        if tmp != -1:
            i = 3
            if isTwo(content[tmp-3]):
                i = 2
            bookDict[bookTxt[0:-4]] = [content[tmp-i:tmp]]
            continue
        tmp = content.find('创作')
        if tmp != -1:
            i = 3
            if isTwo(content[tmp-3]):
                i = 2
            bookDict[bookTxt[0:-4]] = [content[tmp-i:tmp]]
            continue
    with open(os.path.join(stanfordDir,bookTxt),'r',encoding='utf-8') as txtFile:
        nerList = txtFile.readlines()
        flag = False
        for ner in nerList:
            ner = ner.replace('(','').replace(')','').replace('\n','').replace('\'','').replace('\'','').split(',')
            if ner[1] == ' PERSON':
                bookDict[bookTxt[0:-4]] = [ner[0]]
                flag = True
                break
        if flag == False:
            bookDict[bookTxt[0:-4]] = ['']

def findTorTg(nerList):
    for ner in nerList:
        ner = ner.replace('\n', '').split('/')
        if len(ner)<2:
            return ''
        if ner[1] == 't' or ner[1] == 'tg':
            return ner[0]
    return ''

def findNs(nerList):
    for ner in nerList:
        ner = ner.replace('\n', '').split('/')
        if len(ner)<2:
            return ''
        if ner[1] == 'ns' and ner[0] != '中国':
            return ner[0]
    return ''

for bookTxt in pyhanlpBookTxtList:
    with open(os.path.join(pyhanlpDir,bookTxt),'r',encoding='utf-8') as txtFile:
        nerList = txtFile.readlines()
        # print(type(bookDict[bookTxt[0:-4]]))
        bookDict[bookTxt[0:-4]].append(findTorTg(nerList))
        bookDict[bookTxt[0:-4]].append(findNs(nerList))

print(1)

import json

with open('./data/GIS1.0.json','w',encoding='utf-8') as jsonFile:
    json.dump(bookDict,jsonFile,indent=4,ensure_ascii=False)

# index = 0
# for key,value in bookDict.items():
#     if len(value) != 0:
#         print(key+'\t'+str(value))
#         index += 1
# print(index)