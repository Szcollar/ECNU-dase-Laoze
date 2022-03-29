from getAuthorSQLData import *
import pymysql
import re

sub = re.compile(r'[^\x00-\x7f]')

dataList = getData()

# print(bytes(dataList[204][3], 'utf-8').decode('utf-8', 'ignore'))


db = pymysql.connect(host='localhost',user='root',password='123456',database='laozi',charset='utf8')

cursor = db.cursor()

sql = """create table author(
id int(11) primary key,
author_name varchar(22),
author_dynasty varchar(22),
author_intro longtext,
author_pic varchar(255)
)"""

sql = "insert into author values(%s,%s,%s,%s,%s)"

cursor.executemany(sql,dataList)
db.commit()