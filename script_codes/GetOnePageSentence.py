from bs4 import BeautifulSoup
import askurl
import re
from selenium import webdriver

baseurl = 'http://bcc.blcu.edu.cn'

findPC = re.compile(r'<!-- PC端 -->(.*?)<!-- 手机端 -->',re.S)
findsen = re.compile(r'<tr class="hide-mobile" style="display: block; width:100%">(.*?)</tr>',re.S)
findlink = re.compile(r'href="(.*?)">全文</a>')
findtitle = re.compile(r'<b>(.*?)</b>',re.S)
findbody = re.compile(r'</b>(.*?)</div>',re.S)
delbody = re.compile(r'<(.*?)>')

def GetSentence(url):
    SenList = []
    html = askurl.askURL(url)
    soup = BeautifulSoup(html, 'html.parser')
    soup = str(soup.find_all('div',class_ = 'modal-body'))
    title = re.findall(findtitle,soup)[0]+'\n'
    body = re.findall(findbody,soup)[0]
    body = re.sub(delbody,'',body).replace('\r','').replace(' ','')
    if body[-1] != '\n':
        body+='\n'
    SenList.append(title)
    SenList.append(body)
    return SenList

def GetWordList(html,number = None):
    linklist = []
    data=[]
    soup = BeautifulSoup(html, 'html.parser')
    soup = str(soup.find_all('table',class_ = 'table table-striped'))
    temphtml = re.findall(findPC,soup)[0]
    if temphtml == '\n':
        return data
    senhtmlist = re.findall(findsen,temphtml)
    for link in senhtmlist:
        linklist.append(baseurl + re.findall(findlink,link)[0])

    #控制爬取多少数据
    flag = False
    if(number != None):
        flag = True

    for link in linklist:
        data.append(GetSentence(link))

        # 控制爬取多少数据
        if flag:
            number -= 1
            if number == 0:
                break

    # print(data)
    return data

# url = 'http://bcc.blcu.edu.cn/zh/search/0/%E5%87%BA%E7%94%9F%E5%85%A5%E6%AD%BB'
# browser = webdriver.Chrome()
# browser.get(url)
# print(GetWordList(browser.page_source))