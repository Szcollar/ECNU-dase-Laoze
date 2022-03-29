from bs4 import BeautifulSoup
import askurl
import re
from urllib.parse import quote, unquote

findContent = re.compile(r'<div class="para" label-module="para">(.*?)</div>',re.S)
findExplain = re.compile(r'意思(.*?)。',re.S)
findExplain1 = re.compile(r'是指(.*?)。',re.S)
findExplain_ = re.compile(r'意思(.*?)。出自',re.S)
findExplain1_ = re.compile(r'是指(.*?)。出自',re.S)
findExplain__ = re.compile(r'意思(.*?)，出自',re.S)
findExplain1__ = re.compile(r'是指(.*?)，出自',re.S)

findSub = re.compile(r'<(.*?)>',re.S)


def getData(url):
    html = askurl.askURL(url)
    soup = BeautifulSoup(html, 'html.parser')
    soup = str(soup.find_all('div',class_ = 'lemma-summary'))
    content = re.findall(findContent,soup)
    if len(content) == 0:
        return [],0
    content = content[0]
    content = re.sub(findSub,'',content)
    flag = 0
    if content.find('汉语成语') >= 0:
        flag = '汉语成语'
    elif content.find('汉语词汇') >= 0:
        flag = '汉语词汇'


    explain = re.findall(findExplain__,content)
    pass
    if len(explain) == 0:
        explain = re.findall(findExplain1__, content)
    if len(explain) == 0:
        explain = re.findall(findExplain_, content)
    if len(explain) == 0:
        explain = re.findall(findExplain1_,content)
    if len(explain) == 0:
        explain = re.findall(findExplain,content)
    if len(explain) == 0:
        explain = re.findall(findExplain1,content)
    if len(explain) == 0:
        return [],0
    return explain,flag

# idiom = '信口胡言'
# url = quote(idiom, safe=";/?:@&=+$,", encoding="utf-8")
# url = 'https://baike.baidu.com/item/'+url
#
# print(getData(url))

# print('https://baike.baidu.com/item/'+url)
# print(getData('https://baike.baidu.com/item/'+url))


# soup = getData('https://baike.baidu.com/item/'+url)
# soup = str(soup.find_all('div',class_ = 'lemma-summary'))
# content = re.findall(findContent,soup)
# # print(content)
#
# explain = re.findall(findExplain,content[0])
#
# if len(explain) == 0:
#     explain = re.findall(findExplain1,content[0])
#
# print(explain[0])
#
# # print(re.findall(findExplain,content[0])[0])
# # print(soup)