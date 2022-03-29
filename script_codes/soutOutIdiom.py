import pypinyin
import pymysql
import csv

idiomPath = './data/idiom.csv'

db = pymysql.connect(host='localhost',user='root',password='123456',database='laozi',charset='utf8')

cursor = db.cursor()

# sql = """create table idiom(
# id int(11) primary key,
# firstPhonetic varchar(255),
# idiom varchar(255) NOT NULL,
# idiomPhonetic varchar(255),
# simplePhonetic varchar(255),
# explanation varchar(255),
# allusion varchar(255),
# example longtext,
# similar varchar(255),
# grammar varchar(255),
# translation varchar(255),
# antonym varchar(255),
# structure varchar(255),
# ismodern varchar(255),
# frequency varchar(255),
# feeling varchar(255)
# )"""
#
# sql = sql.replace('varchar(255)','longtext')
#
# cursor.execute(sql)

def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s

dataList = []
index = 0
with open(idiomPath,'r',encoding='utf-8') as csvFile:
    csvReader = csv.reader(csvFile)
    header = next(csvReader)[0:-6]
    # print(header)
    for row in csvReader:
        dataList.append((str(index),pinyin(row[0][0]),*tuple(row[0:-6])))
        index += 1

sql = 'INSERT INTO idiom VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

# print(dataList)
cursor.executemany(sql,dataList)
db.commit()