import pymysql
import json

db = pymysql.connect(host='localhost',user='root',password='123456',database='laozi',charset='utf8')

cursor = db.cursor()

sql = """create table laozi_idiom(
id int(11) primary key,
idiom varchar(22),
original varchar(55),
para int(11),
explaination longtext
)
"""

sql = 'INSERT INTO laozi_idiom(id,idiom,original,para,explaination) VALUES(%s,%s,%s,%s,%s)'

dataDict = {}

string = "<li><button onclick=\"selectIdiom(%s)\">%s</button></li>"

with open('./data/data.json','r',encoding='utf-8') as jsonFile:
    dataDict = json.load(jsonFile)

dataList = []
index = 0
for idiomDict in dataDict:
    temp = string%(str(index),idiomDict['chengyu'])
    # dataList.append((str(index),idiomDict['chengyu'],idiomDict['ttk'],idiomDict['para'],idiomDict['trans'][0]['text']))
    index += 1
    with open("./dataScientist.txt",'a',encoding='utf-8') as txtFile:
        txtFile.write(temp+'\n')

# cursor.executemany(sql,dataList)
# db.commit()







# cursor.execute(sql)
# db.commit()