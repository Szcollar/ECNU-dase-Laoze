import os
import json
import copy

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

laoziList = [tuple(dictdata.values()) for dictdata in data]


dataPath = './data/chengyu_1.json'

data = None
with open(dataPath,'r',encoding='utf-8') as jsonFile:
    data = json.load(jsonFile)
temp = data[1]

jsonData = []
jsonData.append(data[0])
index = 0
for row in laoziList:
    tmp = copy.deepcopy(temp)
    tmp['p']['segments'][0]['start']['identity'] = 'Idiom'+str(index)
    tmp['p']['segments'][0]['start']["properties"]["name"] = row[0]
    tmp['p']['segments'][0]['start']["properties"]["explan"] = row[1]
    tmp['p']['segments'][0]["relationship"]['start'] = 'Idiom'+str(index)
    index += 1
    jsonData.append(copy.deepcopy(tmp))

with open('./data/chengyu_11.json','w',encoding='utf-8') as jsonFile:
    json.dump(jsonData,jsonFile,indent=4,ensure_ascii=False)