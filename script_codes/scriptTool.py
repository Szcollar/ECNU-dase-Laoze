import urllib.request,urllib.error
import time
import urllib.request
from bs4 import BeautifulSoup
import os
import re



def askURL(url):
    # time.sleep(2)
    head={         #模拟浏览器头部信息，向豆瓣服务器发送消息
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 86.0.4240.111 Safari / 537.36'
    }   #用户代理表示告诉客户端，我们是什么类型的机器，浏览器，本质上是告诉浏览器我们可以接受什么水平的文件内容
    #key值一定要打对，没有空格
    request=urllib.request.Request(url,headers=head)
    html=''
    while True:
        try:
            response = urllib.request.urlopen(request,timeout=15)
            html=response.read()#.decode('utf-8')
            return html
            # print(html)
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print('error',e.code)
            if hasattr(e,'reason'):
                print('error',e.reason)

def encodeChinese(word):
    return urllib.request.quote(word)

def getSoup(url):
    html = askURL(url)
    soup = BeautifulSoup(html,'html.parser')
    return soup

def confirmDir(dirPath):
    if not os.path.exists(dirPath):
        os.mkdir(dirPath)

def tagHasAttr(tag,attr=None):
    tag = re.findall('<(.*?)>',tag)[0]
    tagList = tag.split(' ')
    if attr == None:
        return len(tagList) == 1
    else:
        for i in range(1,len(tagList)):
            lenth = len(attr)
            if tagList[i].split('=')[0] == attr:
                return True
    return False

def getTitle(tag):
    if tag == 'None':
        return ''
    if tagHasAttr(tag):
        return re.findall('>(.*?)<',tag)[0]
    else:
        return ''

def getBaiduContent(contentList):
    ans = ''
    temp = ''
    for content in contentList:
        content = re.sub('<(.*?)>','',str(content))
        content = re.sub('\[(.*?)\]', '', str(content))
        temp += content
    ansList = temp.split('\n')
    # print(ansList)
    for row in ansList:
        if row != '' and row != '\xa0':
            ans = ans + row + '\n'
    return ans

def getFromBaidu(item):
    dataList = []
    url = 'https://baike.baidu.com/item/'+encodeChinese(item)
    soup = getSoup(url)
    title = getTitle(str(soup.find('h1')))
    subtitle = getTitle(str(soup.find('h2')))
    content = getBaiduContent(soup.find_all('div',class_="lemma-summary"))
    return title,subtitle,content


# soup=getFromBaidu('高抬贵手')
# print(soup)