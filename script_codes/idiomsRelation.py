import os

baseResPath = './data/res.txt'

bookDict = {}

# with open(baseResPath,'r',encoding='utf-8') as txtFile:
#     origins = txtFile.readlines()
#     for row in origins:
#         rowList = row.split(' ')
#         if len(rowList) <= 2:
#             continue
#         for i in range(1,len(rowList)-1):
#             key = os.path.join('.',rowList[i])
#             bookDict.setdefault(key,[])
#             bookDict[key].append(rowList[0])
#
# print(len(bookDict.keys()))
# temp = []
# bookOrigin = []
# index = 0
# for key,value in bookDict.items():
#     if len(value) == 1:
#         temp.append(key)
#         continue
#     if key.split('\\')[1] == 'ancient_chinese_books':
#         bookOrigin.append(key)
#     else:
#         index += 1
# for key in temp:
#     del bookDict[key]
# print(len(bookDict.keys()))
#
#
#
# for key,value in bookDict.items():
#     print(key+'\t',value)

with open(r'C:\Users\lenovo\Desktop\data_project\data\ancient_chinese_books\首页\儒藏\礼经\郊社禘祫问\原文.txt','r',encoding='utf-8') as txtFile:
    temp = txtFile.readlines()
    print(temp)
    for row in temp:
        print(row)
