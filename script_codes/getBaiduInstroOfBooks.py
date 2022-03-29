from bs4 import BeautifulSoup
from scriptTool import *
import re
from countBooksNum import *

baseDir = './data/baiduInstro'

getNums(baseIncoreDir,'./data/ancient_chinese_books')
sub = re.compile(r'<(.*?)>',re.S)
sub_ = re.compile(r'/[(.*?)/]',re.S)


baseUrl = 'https://baike.baidu.com/item/'

def writeInTxt(book,content):
    txtPath = os.path.join(baseDir,book+'.txt')
    with open(txtPath,'w',encoding='utf-8') as txtFile:
        txtFile.write(content)

def getStr(url):
    soup = getSoup(url)
    soup = soup.find_all('div',class_ = 'lemma-summary')
    soup = str(soup)
    soup = re.sub(sub,'',soup)
    return soup

def writeInLog(book):
    path = os.path.join(baseDir,'log.txt')
    with open(path,'a',encoding='utf-8') as txtFile:
        txtFile.write(book+'\n')

sdf = 1

for book in bookList:
    url = baseUrl+encodeChinese(book)
    soup = getStr(url)
    if len(soup)<5:
        writeInLog(book)
        continue
    writeInTxt(book,soup[2:-1])
    print(book)