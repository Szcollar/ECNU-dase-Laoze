from bs4 import BeautifulSoup
from scriptTool import *
import re
from countBooksNum import *

txtPath = './data/bookToDynasty.txt'

getNums(baseIncoreDir,'./data/ancient_chinese_books')
sub = re.compile(r'<(.*?)>',re.S)
sub_ = re.compile(r'/[(.*?)/]',re.S)

dynastyList = ['前蜀','后蜀','杨吴','南唐','吴越','闽','南北朝','马楚','南汉','南平','北汉','后梁','后唐','后晋','后汉','后周','北宋','南宋','宋','隋','唐','元','明','清','春秋','战国','西汉','东汉','汉','夏','商','西周','东周','周','秦','三国','魏','蜀','吴','北魏','东魏','西魏','北齐','刘宋','萧齐','萧梁','南陈','北周','西晋','东晋','晋','五胡','南北朝','南朝','北朝','五代','五代','后梁','后唐','后晋','后汉','后周','十国','辽','西夏','金']
dynastySet = set(dynastyList)

baseUrl = 'https://baike.baidu.com/item/'

def writeInTxt(book,dynasty):
    with open(txtPath,'a',encoding='utf-8') as txtFile:
        txtFile.write(book+'\t'+dynasty+'\n')

def getStr(url):
    soup = getSoup(url)
    soup = soup.find_all('div',class_ = 'lemma-summary')
    soup = str(soup)
    soup = re.sub(sub,'',soup)
    return soup

def find_chaodai(soup):
    for i in range(len(soup)):
        for L in range(1,4):
            if i+L<len(soup) and soup[i:i+L] in dynastySet:
                return soup[i:i+L]
    return "unknow"

sdf = 1

for book in bookList:
    url = baseUrl+encodeChinese(book)
    soup = getStr(url)
    dynasty = find_chaodai(soup)
    writeInTxt(book,dynasty)
    print(book+'\t'+dynasty)