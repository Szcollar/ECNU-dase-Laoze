from scriptTool import *
import os
import json

jsonPath = './data/GISdata/GIS1.0.json'
dataDir = './data/GISdata/author'
confirmDir(dataDir)
dataDict = {}
logPath = './data/GISdata/author/withoutAuthorLog.txt'

with open(jsonPath,'r',encoding='utf-8') as jsonFile:
    dataDict = json.load(jsonFile)

def writeInLog(book):
    with open(logPath,'a',encoding='utf-8') as txtFile:
        txtFile.write(book+'\n')

def writeInFile(title,subtitle,content,book):
    bookPath = os.path.join(dataDir,book+'.txt')
    with open(bookPath,'w',encoding='utf-8') as txtFile:
        txtFile.write(title+'\t'+subtitle+'\n')
        txtFile.write(content+'\n')

# for key,value in dataDict.items():
#     print(key)
#     if value[0] == '':
#         writeInLog(key)
#         continue
#     title,subtitle,content = getFromBaidu(value[0])
#     writeInFile(title,subtitle,content,key)
print(getFromBaidu("李百药"))