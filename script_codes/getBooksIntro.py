from scriptTool import *
from bs4 import BeautifulSoup
import os
import urllib.request
import re

baseUrl = 'https://so.gushiwen.cn/guwen/Default.aspx?p=1&type='
oneBaseUrl = 'https://so.gushiwen.cn'

baseDir = './data/BookIntro'

sections = ['经部','史部','子部','集部']

findDynasty = re.compile(r'</a>(.*?)</span>',re.S)
findBookName = re.compile(r'target="_blank">(.*?)</a>',re.S)
findIntroUrl = re.compile(r'<a href="(.*?)"',re.S)
findOneIntro = re.compile(r'<p style=" margin:0px;">(.*?)<a href=',re.S)
findOneIntro_ = re.compile(r'<p style=" margin:0px;">(.*?)</a>',re.S)
findOneIntro__ = re.compile(r'<p style=" margin:0px;">(.*?)</p>',re.S)
subUrl = re.compile(r'<a(.*?)</a>',re.S)


def getDataList(pageNum):
    url = baseUrl + encodeChinese(sections[pageNum])
    soup = getSoup(url)
    soupStr = str(soup.find_all('div',style="border:0px;"))
    soupStr = soupStr.replace('(','').replace(')','')
    return [re.findall(findBookName,soupStr),re.findall(findDynasty,soupStr),re.findall(findIntroUrl,soupStr)]

def getOneIntro(url):
    soup = getSoup(url)
    soupStr = str(soup.find_all('p',style=" margin:0px;"))
    soupStr = re.sub(subUrl,'',soupStr)
    content = re.findall(findOneIntro,soupStr)
    if len(content) == 0:
        content = re.findall(findOneIntro_,soupStr)
    if len(content) == 0:
        content = re.findall(findOneIntro__,soupStr)
    return content[0].replace('\u3000','').replace(' ','').replace('\n','')

# print(getOneIntro('https://so.gushiwen.cn/guwen/book_46653FD803893E4F6D258172C3E6951F.aspx'))

def writeInTxt(path,bookName,dynasty,content):
    txtPath = os.path.join(path,bookName+'('+dynasty+')'+'.txt')
    with open(txtPath,'w',encoding='utf-8') as txtFile:
        txtFile.write(content)

if __name__ == '__main__':
    confirmDir(baseDir)
    for i in range(0,4):
        sectionDir = os.path.join(baseDir,sections[i])
        confirmDir(sectionDir)
        dataList = getDataList(i)
        if len(dataList[0]) != len(dataList[1]) or len(dataList[0]) != len(dataList[2]):
            print('data is error')
            break
        for index in range(len(dataList[0])):
            print('正在获取'+sections[i]+'的'+dataList[0][index])
            writeInTxt(sectionDir,dataList[0][index],dataList[1][index],getOneIntro(oneBaseUrl+dataList[2][index]))