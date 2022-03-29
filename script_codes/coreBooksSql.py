from readCoreBooks import *
import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',database='laozi',charset='utf8mb4')

cursor = db.cursor()

# sql = """create table core_content_data(
# id int(11) primary key,
# subook_id varchar(22),
# subook_name varchar(22),
# subsubook_name varchar(22),
# content longtext,
# translation longtext
# )
# """

sql = "INSERT INTO core_books_data(id,book_id,book_name,category,dynasty,introduction) VALUES(%s,%s,%s,%s,%s,%s)"
# sql = "ALTER TABLE core_content_data DROP category"
temp = []
for data in bookDataList:
    temp.append((data[0][4:],*data))
    # index += 1
temp = tuple(temp)

# for row in temp:
#     if len(row) != 6:
#         print(row)

cursor.executemany(sql,temp)
db.commit()

# cursor.execute(sql)
# db.commit()