import os

baseIncoreDir = './data/ancient_chinese_books/首页'
baseCoreDir = './data/BookIntro'

bookList = []

def getNums(path,fatherPath):
    if not os.path.isdir(path):
        bookList.append(fatherPath.split('\\')[-1])
        return 1
    sum =0
    sections = os.listdir(path)
    for section in sections:
        if section == '译文.txt':
            continue
        sum += getNums(os.path.join(path,section),path)
    return sum

print(getNums('./data/books','./data'))

# if __name__ == '__main__':
#
#     print('./data/ancient_chinese_books/首页/佛藏\t',getNums('./data/ancient_chinese_books/首页/佛藏','./data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/儒藏\t',getNums('./data/ancient_chinese_books/首页/儒藏','./data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/医藏\t',getNums('./data/ancient_chinese_books/首页/医藏','./data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/史藏\t',getNums('./data/ancient_chinese_books/首页/史藏','./data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/子藏\t',getNums('./data/ancient_chinese_books/首页/子藏','./data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/易藏\t',getNums('./data/ancient_chinese_books/首页/易藏','./data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/艺藏\t',getNums('./data/ancient_chinese_books/首页/艺藏','./data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/诗藏\t',getNums('./data/ancient_chinese_books/首页/诗藏', './data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/道藏\t',getNums('./data/ancient_chinese_books/首页/道藏', './data/ancient_chinese_books/首页'))
#     print('./data/ancient_chinese_books/首页/集藏\t',getNums('./data/ancient_chinese_books/首页/集藏', './data/ancient_chinese_books/首页'))
#
#     print('\n'*4)
#
#     txtPath = './data/bookToDynasty.txt'
#     dataDict = {}
#     dataList = []
#     with open(txtPath,'r',encoding='utf-8') as txtFile:
#         dataList = txtFile.readlines()
#     for data in dataList:
#         data = data.split('\t')
#         if dataDict.get(data[1].replace('\n',''),'qweqwe') == 'qweqwe':
#             dataDict[data[1].replace('\n','')] = 1
#         else:
#             dataDict[data[1].replace('\n','')] += 1
#     for key in dataDict.keys():
#         print(key+'\t',dataDict[key])
#
