from readIdiomRelations import getData
import pymysql


dataList = getData()
# print(dataList[1])

db = pymysql.connect(host='localhost',user='root',password='123456',database='laozi',charset='utf8')

cursor = db.cursor()

sql = """create table idiom_relation(
id int(11) primary key,
idiom varchar(255),
book varchar(255),
author varchar(255)
)
"""

sql = 'insert into idiom_relation values(%s,%s,%s,%s)'

# cursor.execute(sql)

cursor.executemany(sql,dataList)
db.commit()