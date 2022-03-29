import os
import json
from geopy.geocoders import Nominatim

baseDir = './data/GISdata/GIS2.0'

bookList = os.listdir(baseDir)
del bookList[0]

geolocator = Nominatim(user_agent='myuseragent')
dynastyList = ['西晋','东晋','西汉','东汉','北宋','南宋','宋','隋','唐','元','明','清','汉','商','秦','晋']
dynastySet = tuple(dynastyList)
dynastyDict = {'西晋':['洛阳','289'],'东晋':['南京','369'],'西汉':['西安','-97'],'东汉':['洛阳','108'],'秦':['洛阳','-214'],'北宋':['开封','1044'],'南宋':['杭州','1203'],'宋':['开封','1044'],'隋':['洛阳','599'],'唐':['西安','762'],'元':['北京','1319'],'明':['北京','1506'],'清':['北京','1774'],'汉':['西安','-97'],'晋':['洛阳','289']}


dataDict = {}


def fun():
    for book in bookList:
        print(book)
        with open(os.path.join(baseDir,book),'r',encoding='utf-8') as txtFile:
            try:
                local,time = tuple(txtFile.read().split('\t'))
                if len(local)>10:
                    local = local.split(' ')[0]
                    if len(local)>10:
                        local = ''
            except ValueError:
                print(book)
            try:
                localtion = geolocator.geocode(local)
            except Exception:
                dataDict[book[0:-4]] = ['',time]
                continue
            if hasattr(localtion,'address') == True:
                if len(localtion.address) < 4:
                    dataDict[book[0:-4]] = ['']
                else:
                    if localtion.address[-2:] == '中国':
                        dataDict[book[0:-4]] = [localtion.address]
                    else:
                        dataDict[book[0:-4]] = ['']
            else:
                dataDict[book[0:-4]] = ['']
            dataDict[book[0:-4]].append(str(time))
            with open('./data/GISdata/GIS2.0(section).txt', 'a', encoding='utf-8') as jsonFile:
                jsonFile.write(book[0:-4]+'\t'+dataDict[book[0:-4]][0]+'\t'+dataDict[book[0:-4]][1]+'\n')


with open('./data/GISdata/GIS1.0.json','r',encoding='utf-8') as jsonFile:
     GISDict = json.load(jsonFile)


with open('./data/GISdata/GIS2.0(section).txt','r',encoding='utf-8') as txtFile:
    temp = txtFile.readlines()
    for row in temp:
        row =row.split('\t')
        if len(row[1]) > 1 and len(row[2]) > 1:
            dataDict[row[0]] = [row[1],row[2]]
            continue
        if len(row[1]) > 1:
            if len(GISDict[row[0]][1]) > 1:
                if GISDict[row[0]][1][0:2] in dynastySet:
                    dataDict[row[0]] = [row[1],dynastyDict[GISDict[row[0]][1][0:2]][1]]
                    continue
            if len(GISDict[row[0]][1]) > 0:
                if GISDict[row[0]][1][0] in dynastySet:
                    dataDict[row[0]] = [row[1],dynastyDict[GISDict[row[0]][1][0]][1]]
                    continue

tempDict = {}
for key,value in GISDict.items():
    print(key)
    if key not in dataDict:
        if len(value[1]) != 0 and len(value[2])!=0:
            if len(value[1]) > 1:
                if value[1][0:2] in dynastySet:
                    localtion = geolocator.geocode(value[2])
                    if hasattr(localtion, 'address') == True:
                        if len(localtion.address) < 4:
                            continue
                        else:
                            if localtion.address[-2:] == '中国':
                                dataDict[key] = [localtion.address,dynastyDict[value[1][0:2]][1]]
                                # dataDict[book[0:-4]] = [localtion.address]
                            else:
                                continue
                    # dataDict[row[0]] = [row[1], dynastyDict[value[1][0:2]][1]]
            elif len(value[1]) > 0:
                if value[1][0] in dynastySet:
                    localtion = geolocator.geocode(value[2])
                    if hasattr(localtion, 'address') == True:
                        if len(localtion.address) < 4:
                            continue
                        else:
                            if localtion.address[-2:] == '中国':
                                dataDict[key] = [localtion.address, dynastyDict[value[1][0]][1]]
                                # dataDict[book[0:-4]] = [localtion.address]
                            else:
                                continue
                    # dataDict[row[0]] = [row[1], dynastyDict[value[1][0]][1]]


with open('./data/GISdata/GIS2.0.json','w',encoding='utf-8') as jsonFile:
    json.dump(dataDict,jsonFile,indent=4,ensure_ascii=False)
# localtion  = geolocator.geocode('河北, 合肥市, 安徽省, 230001, 中国')
# print(localtion.address)
# print(hasattr(localtion,'address'))

