import pymysql
import json

jsonData = {}
languageList = ['French','German','Hebrew','Hungarian','Icelandic','Indonesian','Interlingua','Italian','Japanese','Klingon','Korean','Kurdish','Latvian','Persian','Phoenician','Polish','Romanian','Russian','Spanish','Swedish']
dataDict = {}

with open('./data/Translation.json','r',encoding='utf-8') as jsonFile:
    jsonData = json.load(jsonFile)

# <option value="volvo">Volvo</option>

for key,value in jsonData.items():
    print("<option value=\"{}\">{}</option>".format(key,key))
    # print('private String '+key+';')
    # dataDict[key] = []
    # for _,translation in value.items():
    #     for chapter,chapterTranslation in translation.items():


db = pymysql.connect(host='localhost',user='root',password='123456',database='laozi',charset='utf8mb4')

cursor = db.cursor()

sql = """create table daodejing(
chapter int(11) primary key,
original longtext,
translation longtext,
annotation longtext
)
"""

sql = "INSERT INTO daodejing({}) VALUES('%s') where chapter={}"
sql = "UPDATE daodejing SET {}='%s' WHERE chapter={}"

# for language in languageList:
#     for key in jsonData[language].keys():
#         data = []
#
#         for k,v in jsonData[language][key].items():
#             tempSQL = sql.format(language,k)%v.replace('\n','').replace('\'',r'\'')
#             cursor.execute(tempSQL)
#             db.commit()
#         break



# for i in dataList:
#     print(i)

# cursor.executemany(sql,languageList)
# db.commit()

# cursor.execute(sql)
# db.commit()