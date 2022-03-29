import os
from scriptTool import *
import re

baseUrl = 'http://www.guoxuedashi.net/chengyu/'

findPyLink = re.compile(r'href="/chengyu(.*?)" target="_blank">',re.S)
findLetter = re.compile(r'width="20">(.*?)</td><td>',re.S)
findPy = re.compile(r'html" target="_blank">(.*?)</a>',re.S)

def getRawSoup(url):
    soup = getSoup(url)
    indexTable = soup.find_all('table',class_="table2")
    return indexTable[0],indexTable[1]

pyTable,secTable = getRawSoup(baseUrl)


def sortOutPyTable(pyTable):
    dataList = []
    pyTableList = str(pyTable).split('\n')
    # print(pyTableList)
    for row in pyTableList[1:-1]:
        # print(row)
        letter = re.findall(findLetter,row)[0]
        pyLinkList = re.findall(findPyLink,row)
        pyList = re.findall(findPy,row)
        dataList.append({letter : [(pyList[i],pyLinkList[i]) for i in range(len(pyList))]})
    return dataList




