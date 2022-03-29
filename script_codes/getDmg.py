import os

import requests
from bs4 import BeautifulSoup

def download_img(img_url,path):
    ret = requests.get(img_url)
    # 图片信息
    info = ret.content
    # 二进制方式写入
    with open(path, 'wb') as f:
        f.write(info)

# download_img('https://song.gushiwen.cn/authorImg/xunzi.jpg','./荀子.jpg')