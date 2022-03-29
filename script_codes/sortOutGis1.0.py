import os
import re

temp = '''张岱	（明末清初史学家、文学家）
张岱生于明隆庆四年（1570年），卒于明崇祯十五年（1642年），一名维城，字宗子，又字石公，号陶庵、陶庵老人、蝶庵、古剑老人、古剑陶庵、古剑陶庵老人、古剑蝶庵老人，晚年号六休居士，、出生于南京，祖籍四川绵竹（故自称“蜀人”）
，明清之际史学家、文学家。张岱出身仕宦家庭，早年患有痰疾而长住外祖父陶大顺家养病，因聪颖善对而被舅父陶崇道称为“今之江淹”，提出过“若以有诗句之画作画，画不能佳；以有诗意之诗为诗，诗必不妙”等观点；于天启年间和崇祯初年悠游自在，创作了许多诗文；于崇祯八年（1635年）参加乡试，因不第而未入仕；明亡后，避兵灾于剡中，于兵灾结束后隐居四明山中，坚守贫困，潜心著述，著有《陶庵梦忆》和《石匮书》等；康熙四年（1665年）撰写《自为墓志铭》，向死而生；后约于康熙二十八年（1689年）与世长辞，享年约九十三岁，逝后被安葬于山阴项里。史学上，张岱与谈迁、万斯同、查继佐并称“浙东四大史家”；文学创作上，张岱以小品文见长，以“小品圣手”名世。（概述图片来源：《张岱》
）
'''

temp = '''北齐	
北齐（550年～577年），是中国南北朝时期的北朝政权之一，由东魏权臣高欢次子高洋所建。历经六帝，享国二十八年。
东魏权臣高欢死后，长子高澄继专魏政，将篡未篡之时，被家奴刺杀。
其弟高洋袭位，废掉东魏的傀儡皇帝孝静帝，于550年（庚午年五月戊午日），
即帝位，国号齐，建元天保，
建都邺城，史称北齐。因皇室姓氏为高氏，故又称高齐。
北齐继承了东魏所控制的地盘，占有今黄河下游流域的河北、河南、山东、山西以及苏北、皖北的广阔地区。同时与其并存的王朝有西魏、北周（取代西魏）、梁、陈（取代梁，但只占有前者部分领土）等。北齐天保三年（552年）以后，北击库莫奚、东北逐契丹、西北破柔然，
西平山胡，
南取淮南，势力一直延伸到长江边，这时北齐的国力达到鼎盛。武成帝昏庸好色，
北齐国力大衰，不久去世，由后主高纬继立。高纬也是昏庸好色，国政混乱，
还诛杀名将斛律光。
之后北齐被南陈攻下淮南，并在577年亡于北周。北齐的核心主要为六镇流民及关东世族，
其军力比较强盛。由于其源头六镇流民偏向鲜卑化以及统治者为鲜卑化汉人的原因，使得北齐主要提倡鲜卑文化。北齐的农业、盐铁业、瓷器制造业都相当发达，是同陈、北周鼎立的三个国家中最富庶的。北齐继续推行均田制，大体上与北魏相同，但也略有变化。

'''

reg = "[^0-9A-Za-z\u4e00-\u9fa5（）～()－—\-？~?]"
temp = re.sub(reg,' ',temp)
temp = temp.replace('(','（').replace(')','）').replace('～','－').replace('~','－').replace('-','－').replace('?','？').replace('—','－')

baseDir = './data/GISdata'
baseAuthorDir = os.path.join(baseDir,'author')
goalDir = os.path.join(baseDir,'GIS2.0')

province = "江苏省、浙江省、山东省、河南省、湖北省、湖南省、北京市、天津市、上海市、重庆市、河北省、山西省、辽宁省、吉林省、黑龙江省、安徽省、福建省、江西省、广东省、海南省、四川省、贵州省、云南省、陕西省、甘肃省、青海省、台湾省、内蒙古区、广西区、西藏区、宁夏区、新疆区、香港区、澳门区"
provinceList = province.split('、')

def getContent(path):
    with open(path,'r',encoding='utf-8') as txtFile:
        return txtFile.read()

def getLoc(string):
    firstPattern = re.compile("（今属(.*?)）")
    firstAns = re.findall(firstPattern,string)
    if len(firstAns) != 0:
        return firstAns[0]
    secondPattern = re.compile("（今(.*?)）人")
    secondAns = re.findall(secondPattern, string)
    if len(secondAns) != 0:
        return secondAns[0]
    thirdPattern = re.compile("（今(.*?)）")
    thirdAns = re.findall(thirdPattern, string)
    if len(thirdAns) != 0:
        return thirdAns[0]
    forthPattern = re.compile("为(.{1,8})人")
    forthAns = re.findall(forthPattern, string)
    if len(forthAns) != 0:
        return forthAns[0]
    sixPattern = re.compile("出生于(.*?)\s")
    sixAns = re.findall(sixPattern, string)
    if len(sixAns) != 0:
        return sixAns[0]
    pattern = "%s(.*?)人"
    for province in provinceList:
        fifthPattern = pattern % province[0:-1]
        fifthAns = re.findall(fifthPattern, string)
        if len(fifthAns) != 0:
            return fifthAns[0]
    return ''


def getTime(string):
    rawPattern = re.compile("（[^）]*－.*?）")
    rawStr = re.findall(rawPattern,string)
    if len(rawStr) >0:
        rawStr = re.sub("[^\d年月日前？－）]",' ',rawStr[0])
        rawStr = re.sub("年(.*?)[－）]", ' ', rawStr.replace(' ',''))
        rawStr = re.sub("[^\d？前]", ' ', rawStr)
        rawList = rawStr.strip(' ').replace('前','-').split(' ')

        for i in (0,-1):
            if len(rawList[i]) > 1:
                rawList[i] = rawList[i].replace('？','')

        if len(rawList)<2 or rawList[0].isdigit() == False or rawList[1].isdigit() == False:
            pass
        else:
            if rawList[0] == '？':
                rawList[0] = int(rawList[1])-30
            elif rawList[1] == '？':
                rawList[1] = int(rawList[0])+30
            return (int(rawList[0]) + int(rawList[-1]))//2

    otherPattern = re.compile("（(\d*)年）")
    ans = re.findall(otherPattern,string)
    if len(ans) > 2:
        return (int(ans[0])+int(ans[1]))//2
    return ''

def writeInTxt(path,local,time):
    with open(path,'w',encoding='utf-8') as txtFile:
        txtFile.write(local+'\t'+str(time))

def writeInLog(book):
    with open(os.path.join(goalDir,'withoutLog.txt'),'a',encoding='utf-8') as txtFile:
        txtFile.write(book+'\n')

# temp = getContent(os.path.join(baseAuthorDir,'七佛俱胝佛母心大准提陀罗尼法.txt'))
# print(getTime(temp))

if __name__ == '__main__':
    dateList = os.listdir(baseAuthorDir)
    del dateList[0]
    for book in dateList:
        print(book)
        temp = getContent(os.path.join(baseAuthorDir,book))
        if len(temp) < 5:
            writeInLog(book)
            continue
        temp = re.sub(reg, ' ', temp)
        temp = temp.replace('(','（').replace(')','）').replace('~','－').replace('-','－').replace('?','？').replace('—','－')
        local = getLoc(temp)
        time = getTime(temp)
        if local == '' and time == '':
            writeInLog(book)
            continue
        writeInTxt(os.path.join(goalDir,book),local,time)






