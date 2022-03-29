import pymysql
import os
import json
filePath = './data/老子成语.txt'
dataList = []
with open(filePath,'r',encoding='utf-8') as txtFile:
    dataList = txtFile.readlines()
dataList = [line.strip() for line in dataList if len(line.strip())!=0]
data = []

for i in range(0,len(dataList),3):
    tmp={}
    tmp["idiom"] = dataList[i].split('、')[1]
    tmp["explain"] = dataList[i+1][5:]
    source = dataList[i + 2][5:]
    tmp["source_para"] = source[:3]
    tmp["source_sent"] = source[5:-1]
    data.append(tmp)

temp = [tuple(dictdata.values()) for dictdata in data]
print(1)

db = pymysql.connect(host='localhost',user='root',password='123456',database='laozi',charset='utf8')

cursor = db.cursor()

# sql = "alter table laozi_idiom add chinese_tran longtext"
#
# cursor.execute(sql)
# db.commit()

sql = "update laozi_idiom set chinese_tran=\'%s\' where laozi_idiom.idiom = \'%s\'"

for row in temp:
    tmpsql = sql%(row[1],row[0])
    cursor.execute(tmpsql)
    db.commit()

# for i in dataList:
#     print(i)

# cursor.executemany(sql,dataList)
# db.commit()

# cursor.execute(sql)
# db.commit()