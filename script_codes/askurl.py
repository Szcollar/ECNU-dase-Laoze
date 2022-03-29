import urllib.request,urllib.error
import time

def askURL(url):
    time.sleep(0.2)
    head={         #模拟浏览器头部信息，向豆瓣服务器发送消息
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 86.0.4240.111 Safari / 537.36'
    }   #用户代理表示告诉客户端，我们是什么类型的机器，浏览器，本质上是告诉浏览器我们可以接受什么水平的文件内容
    #key值一定要打对，没有空格

    request=urllib.request.Request(url,headers=head)
    html=''
    while True:
        try:
            response = urllib.request.urlopen(request,timeout=15)
            html=response.read()#.decode('utf-8')
            return html
            # print(html)
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print('error',e.code)
            if hasattr(e,'reason'):
                print('error',e.reason)


# print(askURL('https://baike.baidu.com/item/%E7%AB%A5%E7%94%B7%E7%AB%A5%E5%A5%B3'))


