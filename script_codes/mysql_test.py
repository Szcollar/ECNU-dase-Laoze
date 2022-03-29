import pymysql
from readDaodejin import *

dataList = getDaoDeJinSql()
# print(dataList[1])

db = pymysql.connect(host='localhost',user='root',password='123456',database='laozi',charset='utf8')

cursor = db.cursor()

sql = """create table daodejing(
chapter int(11) primary key,
original longtext,
translation longtext,
annotation longtext
)
"""

sql = 'INSERT INTO daodejing(chapter,original,translation,annotation) VALUES(%s,%s,%s,%s)'




# for i in dataList:
#     print(i)

cursor.executemany(sql,dataList)
db.commit()

# cursor.execute(sql)
# db.commit()