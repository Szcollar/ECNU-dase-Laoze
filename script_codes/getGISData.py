# coding:utf-8
import os

baseDir = './data/baiduInstro'
stanford = './data/GISner/stanfordcorenlp'
pyhanlpDir = './data/GISner/pyhanlp'

bookList = os.listdir(baseDir)
del bookList[0]

def getContent(bookTxtName):
    path = os.path.join(baseDir,bookTxtName)
    return open(path,'r',encoding='utf-8').read()

def writeResult(directory,contentList,bookTxt):
    path = os.path.join(directory,bookTxt)
    with open(path,'w',encoding='utf-8') as writeFile:
        for row in contentList:
            writeFile.write(str(row)+'\n')

#person
from stanfordcorenlp import StanfordCoreNLP
print(getContent('撰集百缘经.txt'))
# 加载模型
stanford_model = StanfordCoreNLP(r'./module/stanford-corenlp-4.2.2', lang='zh')
flag = True
# text = "《哀江南赋》是中国南北朝文学家庾信创作的一篇赋。此赋主要是伤悼南朝梁的灭亡和哀叹自己个人身世，陈述了梁朝的成败兴亡，以及侯景之乱和江陵之祸的前因后果，凝聚着作者对故国和人民遭受劫乱的哀伤。全赋内容丰富而深厚，文字凄婉而深刻，格律严整而略带疏放，文笔流畅而亲切感人，如实记录了历史的真相，具有史诗的规模和气魄，故有“赋史”之称。被誉为“庾信《哀江南赋》、颜之推《观我生赋》，两篇实南北朝之大文。"
for bookTxt in bookList:
    if flag == True and bookTxt != '撰集百缘经.txt':
        continue
    flag = False
    print(bookTxt)
    text = getContent(bookTxt)
    res = stanford_model.ner(text)
    writeResult(stanford,res,bookTxt)


# import fool
#
# text = "张三和李四在2019年3月23日在北京的腾讯技术有限公司一起开会。"
#
# res = fool.analysis(text)
# print(res)

#t或者tg
from pyhanlp import *
# 加载模型
ha_model = HanLP.newSegment()
# text = "《哀江南赋》是中国南北朝文学家庾信创作的一篇赋。此赋主要是伤悼南朝梁的灭亡和哀叹自己个人身世，陈述了梁朝的成败兴亡，以及侯景之乱和江陵之祸的前因后果，凝聚着作者对故国和人民遭受劫乱的哀伤。全赋内容丰富而深厚，文字凄婉而深刻，格律严整而略带疏放，文笔流畅而亲切感人，如实记录了历史的真相，具有史诗的规模和气魄，故有“赋史”之称。被誉为“庾信《哀江南赋》、颜之推《观我生赋》，两篇实南北朝之大文。"
for bookText in bookList:
    print(bookText)
    res = list(ha_model.seg(getContent(bookText)))
    writeResult(pyhanlpDir,res,bookText)
# print(str(res[0])[0:2])
# print(str(res[1])[-2:])


# from pyltp import Segmentor, Postagger, NamedEntityRecognizer
# import os
#
# LTP_DATA_DIR = r'./module/ltp_data_v3.4.0'
#
# segmentor = Segmentor()
# segmentor.load(os.path.join(LTP_DATA_DIR, "cws.model"))
#
# postagger = Postagger()
# postagger.load(os.path.join(LTP_DATA_DIR, "pos.model"))
#
# recognizer = NamedEntityRecognizer()
# recognizer.load(os.path.join(LTP_DATA_DIR, "ner.model"))
#
# text = "《哀江南赋》是中国南北朝文学家庾信创作的一篇赋。此赋主要是伤悼南朝梁的灭亡和哀叹自己个人身世，陈述了梁朝的成败兴亡，以及侯景之乱和江陵之祸的前因后果，凝聚着作者对故国和人民遭受劫乱的哀伤。全赋内容丰富而深厚，文字凄婉而深刻，格律严整而略带疏放，文笔流畅而亲切感人，如实记录了历史的真相，具有史诗的规模和气魄，故有“赋史”之称。被誉为“庾信《哀江南赋》、颜之推《观我生赋》，两篇实南北朝之大文。"
#
# words = segmentor.segment(text)
# print(list(words))
# postags = postagger.postag(words)
# print(list(postags))
# netags = recognizer.recognize(words, postags)
# print(list(netags))
#
# for i in range(len(list(words))):
#     if list(postags)[i] == 'nh':
#         print(list(words[i]))