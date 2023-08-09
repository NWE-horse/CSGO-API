# -*- codeing = utf-8 -*-
# @Author :Jnine
# @File : five_e.py
# @Software : PyCharm
import urllib
import string
import bs4
import urllib.request
import json
from urllib import parse
import execjs
from requests import get
import re
from data import utils
import requests


headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.82",
    }
config = utils.get_config()
API = utils.get_api('5e')
def data_5E(name):
    def askurl(name):
        findArg = re.compile(r'var arg1=(.*?);')
        findValue = re.compile(r'<span class="val">(.*?)</span>')
        findGametime = re.compile(r'<span class="val game-time-val">(.*?)</span>')
        findF18 = re.compile(r'<span class="val fs18">(.*?)</span>')
        findF48 = re.compile(r'<span class="val fs48">(.*?)</span>')
        findDesc = re.compile(r'<p class="desc">(.*?)<span>(.*?)</span></p>')
        findClearfix = re.compile(r'<span class="fs14 val">(.*?)</span>')
        findSrc = re.compile(r'src="(.*?)"')
        findHref = re.compile(r'<a href="(.*?)" target="_blank">')
        findHeight = re.compile(r'<video src="(.*?)"')

        # https://arena.5eplay.com/api/search?keywords=
        url = urllib.parse.quote(API['keywords'] + name, safe=string.printable)
        requst = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(requst)
        jsdata = json.loads(response.read().decode("utf-8"))
        try:
            eid = jsdata['data']['user']['list'][0]['domain']
        except IndexError:
            return 'erro'

        def w2_decrypt(arg):
            with open("csgoapi/ws_.js") as f:  # 调用js文件
                jsdata = f.read()
                ctx = execjs.compile(jsdata)
                data = ctx.call('l', arg)
                # print(data)
            return data

        def get_arg():
            # print(url)
            # gzip压缩网页解决方法
            req = get(API['player'] + eid)
            req.encoding = 'utf-8'
            soup = bs4.BeautifulSoup(req.text, 'lxml')
            arg = soup.select('script')[0].text
            # print(arg)
            arg = re.findall(findArg, arg)[0]
            # print(arg)
            return arg

        arg = re.sub("'", "", get_arg())
        w2 = w2_decrypt(arg)

        def get_html(eid):
            cookie = {
                'cookie': 'acw_sc__v2=' + w2}
            req = urllib.request.Request(API['player'] + eid, headers=cookie)
            html = urllib.request.urlopen(req)
            # 获取网站源码
            html = html.read().decode('utf-8')
            soup = bs4.BeautifulSoup(html, 'html.parser')

            def get_val():  # rating数据
                for ur in soup.findAll('ul', class_='stat-data'):
                    ur = str(ur)
                    val = (re.findall(findValue, ur))
                    gametime = re.findall(findGametime, ur)
                    val.append(gametime[0])
                    return val

            def get_pie():  # 饼图
                data = []
                for pie in soup.findAll('div', class_='player-pie-chart fleft posr fs14'):
                    pie = str(pie)
                    player_pie = re.findall(findF18, pie)
                    f48 = re.findall(findF48, pie)
                    player_pie.append(f48[0])
                    return player_pie

            def get_desc():
                desc = soup.findAll('p', class_="desc")
                desc = str(desc)
                data = re.findall(findDesc, desc)
                return data

            def get_clearfix():
                for clearfix in soup.findAll('div', class_='player-feats fleft'):  # 5k
                    clearfix = str(clearfix)
                    data = re.findall(findClearfix, clearfix)
                    return data

            def get_img():
                for img in soup.findAll('img', class_='avatar-img position-center'):
                    img = str(img)
                    src = re.findall(findSrc, img)
                    return src

            def get_item():
                for item in soup.findAll('div', class_='clearfix inner'):  # 高光链接
                    item = str(item)
                    href = re.findall(findHref, item)
                    return href

            try:
                data = get_val(), get_pie(), get_desc()[0], get_clearfix(), get_img()

                info_data = []
                for i in data:
                    for info in i:
                        info_data.append(info)
                return info_data
            except IndexError:
                pass

        return get_html(eid)

    list = askurl(name)
    if list == 'erro':
        return '不存在此ID，请检查你的用户名是否正确！'
    else:
        data = '总排名：{}\n总比赛：{}\n贡献值RWS：{}\n技术得分Rating：{}\n天梯：{}\n游戏时长：{}\n平均每局杀敌：{}\n平均每局助攻：{}\n每局存活率：{}\n' \
               'MPV：{}\nK/D：{}\n爆头率：{}\n胜率：{}\n{}{}\n1V5：{}\n1V4：{}\n1V3：{}\n5K：{}\n4K：{}\n3K：{}\n'
        try:
            result = data.format(*list)
            return result
        except TypeError:
            return '您当前未完成定级赛，完成定级赛后才可查看战绩'

def player_ranking():
    params = {
        "limit": "40",
        "name": "",
        "page": "1"
    }
    response = requests.get(API['playerranking'], headers=headers, params=params)

    player_list = response.json()['data']['items']
    if config['original'] == False:
        rank = ''
        for i in range(10):
            KD = player_list[i]['kd']

            name = player_list[i]['name']

            rating = player_list[i]['rating']

            rank += f'排名：#{i + 1} 【{name}】\nKD：{KD}\nRating：{rating}\n\n'
        return rank
    else:
        return response.json()

def team_ranking():
    params = {
        "page": "1",
        "limit": "10"
    }
    response = requests.get(API['teamranking'], headers=headers, params=params)

    team_list = response.json()['data']['items']
    if config['original'] == False:
        ranking = ''
        for i in range(0, 10):
            name = team_list[i]['name']

            score = team_list[i]['score']

            ranking += f'Rank：{i + 1} Name：{name} 积分：{score}\n'
        return ranking
    else:
        return response.json()