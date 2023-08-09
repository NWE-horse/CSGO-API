# -*- codeing = utf-8 -*-
# @Author :Jnine
# @File : trading.py
# @Software : PyCharm
import re
import urllib
import bs4
import string
from data import utils

config = utils.get_config()
def gun_ie(name):
    findGun = re.compile(r'<div class="name" data-v-c16bddd4="">(.*?)</div>')
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}

    findMoney = re.compile(r'</sup>(.*?)<sub data-v-c16bddd4="">(.*?)</sub>')
    name = urllib.parse.quote(name, safe=string.printable)
    url = 'https://www.igxe.cn/market/csgo?keyword=%s&sort=3&page_size=20' % (name)  # 链接和字符串分离
    urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(url)
    html = html.read().decode('utf-8')
    soup = bs4.BeautifulSoup(html, 'html.parser')
    data = []
    info = ''
    if config['original'] == False:
        for item in soup.findAll('a', class_='item'):
            part_data = []
            item = str(item)
            gun = re.findall(findGun, item)
            part_data.append(gun[0])
            rawmoney = re.findall(findMoney, item)
            money = rawmoney[0][0] + rawmoney[0][1]
            part_data.append(money)
            data.append(part_data)
        for part_info in data:
            info = info + '名称：%s ￥%s元' % (part_info[0], part_info[1]) + '\n'
        return info

    else:
        return soup.text
