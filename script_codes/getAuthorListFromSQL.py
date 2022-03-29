import pymysql

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

sql = 'select author_name from author'


# for i in dataList:
#     print(i)

# cursor.executemany(sql,dataList)
# db.commit()

cursor.execute(sql)
temp = cursor.fetchall()
db.commit()

temp = list(temp)

for i in range(len(temp)):
    temp[i] = temp[i][0]

with open('./data/author/authorList.txt','w',encoding='utf-8') as txtFile:
    for row in temp:
        txtFile.write("\'"+row+"\'"+',')
