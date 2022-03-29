from readIdiomRelations import *

idiomAutherList = getData()

authorSet = []
authorSet = set(authorSet)

for row in idiomAutherList:
    authorSet.add(row[2])

# print(len(idiomAutherList))
print('作者节点数'+'\t',len(authorSet))

resPath = './data/res.txt'
dataList = []
with open(resPath,'r',encoding='utf-8') as txtFile:
    dataList = txtFile.readlines()

bookSet = []
bookSet = set(bookSet)

sum = 0
for row in dataList:
    row = row.split(' ')
    for i in range(1,len(row)-1):
        temp = row[i].split('\\')
        if(len(temp) < 2):
            bookSet.add(temp[0])
            continue
        bookSet.add(row[i].split('\\')[-2])
    sum += len(row)-2

print('书的数量\t',len(bookSet))

print('成语和书的边数\t',sum)

print('边数'+'\t',sum+len(authorSet))