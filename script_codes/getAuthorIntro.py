from askurl import askURL
from getDmg import download_img
import urllib.request
import os
from bs4 import BeautifulSoup
import re

findAuthor = re.compile(r'target="_blank">(.*?)</a></span>',re.S)
findUrl = re.compile(r'href="/(.*?)"',re.S)
findContent = re.compile(r'style=" margin:0px;">(.*?)<a href="',re.S)
findContent_ = re.compile(r'style=" margin:0px;">(.*?)</p>',re.S)
findPicUrl = re.compile(r'src="(.*?)"',re.S)

baseUrl = 'https://so.gushiwen.cn/authors/Default.aspx?p='
dynastyUrl = '&c='
authorUrl = 'https://so.gushiwen.cn/'

baseDir = './data/author'

chineseDynastyList = ['先秦','两汉','魏晋','南北朝','隋代','唐代','五代','宋代','金朝','元代','明代','清代']
dynastyList = ['先秦','两汉','魏晋','南北朝','隋代','唐代','五代','宋代','金朝','元代','明代','清代']

def encodeChinese(wordList):
    for i in range(len(wordList)):
        wordList[i] = urllib.request.quote(wordList[i])

encodeChinese(dynastyList)

def confirmDir(dirPath):
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

def getSoup(page,dynasty):
    url = baseUrl+str(page)+dynastyUrl+dynasty
    html = askURL(url)
    soup = BeautifulSoup(html,'html.parser')
    soup = soup.find_all('div',style="border:0px;")
    return soup

def getIntroUrl(page,dynasty):
    urlList = []
    authorList = []
    soup = getSoup(page,dynasty)
    soup = str(soup)
    urlList = re.findall(findUrl,soup)
    authorList = re.findall(findAuthor,soup)
    return authorList,urlList

def getOneIntro(url):
    html = askURL(url)
    soup = BeautifulSoup(html,'html.parser')
    content = soup.find('p',style=" margin:0px;")
    picUrl = soup.find('img',height="150")
    content_ = re.findall(findContent,str(content))
    if len(content_) == 0:
        content_ = re.findall(findContent_,str(content))[0]
    else:
        content_ = content_[0]

    picUrl = re.findall(findPicUrl, str(picUrl))
    if len(picUrl) == 0:
        picUrl = ''
    else:
        picUrl = picUrl[0]
    return content_,picUrl

# print(getOneIntro('https://so.gushiwen.cn/authorv_75ce8390059f.aspx'))

def getData(page,dynasty):
    dataList = []
    authorList,urlList = getIntroUrl(page,dynasty)
    if len(authorList) != len(urlList):
        print('数量不对！')
        return -1
    for i in range(len(authorList)):
        print(authorList[i])
        url = authorUrl+urlList[i]
        content,picUrl = getOneIntro(url)
        temp=[authorList[i],content,picUrl]
        dataList.append(temp)
    return dataList

def writeInDir(dynasty,dataList):
    dynastyDir = os.path.join(baseDir,dynasty)
    confirmDir(dynastyDir)
    authorDir = os.path.join(dynastyDir,dataList[0])
    confirmDir(authorDir)
    txtPath = os.path.join(authorDir,'introduce.txt')
    picPath = os.path.join(authorDir,dataList[0]+'.jpg')
    with open(txtPath,'w',encoding='utf-8') as txtFile:
        txtFile.write(dataList[1])
    if dataList[2] != '':
        download_img(dataList[2],picPath)

# temp = getData(1,dynastyList[0])
# for row in temp:
#     print(row)

if __name__ == '__main__':
    confirmDir(baseDir)
    for i in range(len(dynastyList)):
        dataList = getData(1,dynastyList[i])
        for temp in dataList:
            writeInDir(chineseDynastyList[i],temp)





