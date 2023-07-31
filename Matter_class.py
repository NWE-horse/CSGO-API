# -*- codeing = utf-8 -*-
# @Time : 2023/7/31 21:19
# @Author :Jnine
# @File : Matter_class.py
# @Software : PyCharm
import urllib
import string
import bs4
import urllib.request
import json
import plotly.graph_objects as go
from PIL import Image, ImageDraw, ImageFont
from urllib import parse
import execjs
from requests import get
import requests
from aiowebsocket.converses import AioWebSocket
import re

def info_wm(id):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://news.wmpvp.com",
        "Referer": "https://news.wmpvp.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
        "X-Requested-With": "XMLHttpRequest",
        "accessToken": "",
        "appversion": "",
        "device": "undefined",
        "platform": "h5_web",
        "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }
    url = "https://api.wmpvp.com/api/v2/csgo/pvpDetailDataStats"

    data = '{"steamId64":"%s","csgoSeasonId":""}' % id

    response = requests.post(url, headers=headers, data=data)

    # 头像图片
    data_avatar = str(response.json()['data']['avatar'])

    # 名字
    data_name = str(response.json()['data']['name'])

    # 赛季场次
    data_cnt = str(response.json()['data']['cnt'])

    # kd
    data_kd = str(response.json()['data']['kd'])

    # winRate
    data_winRate = str(response.json()['data']['winRate'] * 100) + "%"

    # rating
    data_rating = str(response.json()['data']['pwRating'])

    # 总击杀
    data_kills = str(response.json()['data']['kills'])

    # 总助攻
    data_assists = str(response.json()['data']['assists'])

    # 总死亡
    data_deaths = str(response.json()['data']['deaths'])
    # 总mvvp
    data_mvpCount = str(response.json()['data']['mvpCount'])

    # rws
    data_rws = str(response.json()['data']['rws'])

    # adr
    data_adr = str(response.json()['data']['adr'])

    # headShotRatio 爆头率
    data_headShotRatio = str(response.json()['data']['headShotRatio'] * 100) + "%"

    # entryKillRatio 首杀率
    data_entryKillRatio = str(int(response.json()['data']['entryKillRatio']) * 100) + "%"

    # pvpScore
    data_elo = str(response.json()['data']['pvpScore'])

    # summary 评价
    data_summary = str(response.json()['data']['summary'])

    # weaponName 最擅长的武器
    data_weaponName = str(response.json()['data']['hotWeapons'][0]['weaponName'])

    # weaponKill 击杀数
    data_weaponKill = str(response.json()['data']['hotWeapons'][0]['weaponKill'])
    data_result = '游戏名：%s\n天梯分数：%s\n场次：%s\nKD：%s\n胜率：%s\nrating：%s\n总击杀：%s\n总助攻：%s\n总死亡：%s\nmvp次数：%s\nrws：%s\nadr：%s\n爆头率：%s\n首杀率：%s\n你的评价是：%s!' % (
        data_name, data_elo, data_cnt, data_kd, data_winRate, data_rating, data_kills, data_assists, data_deaths,
        data_mvpCount, data_rws, data_adr, data_headShotRatio, data_entryKillRatio,
        data_summary)
    return data_result + data_avatar

def video(id):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Origin": "https://news.wmpvp.com",
        "Referer": "https://news.wmpvp.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.82",
        "X-Requested-With": "XMLHttpRequest",
        "accessToken": "",
        "appversion": "",
        "device": "undefined",
        "platform": "h5_web",
        "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "^\\^Android^^"
    }
    url = "https://appactivity.wmpvp.com/steamcn/video/getPerfectList"

    params = {
        "toSteamId": "%s" % id,
        "token": "",
        "pageNum": "1",
        "pageSize": "10"
    }

    response = requests.get(url, headers=headers, params=params)

    title = response.json()['result']['userVideoList'][0]['title']

    videoURL = response.json()['result']['userVideoList'][0]['videoInfo']['playInfoList'][0]['playURL']

    return title + videoURL

def guns_money(id):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Origin": "https://news.wmpvp.com",
        "Referer": "https://news.wmpvp.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.82",
        "X-Requested-With": "XMLHttpRequest",
        "appversion": "",
        "platform": "h5_web",
        "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "^\\^Android^^",
        "token": ""
    }
    url = "https://gwapi.pwesports.cn/appdecoration/steamcn/csgo/decoration/getSteamInventoryPreview"
    params = {
        "steamId": "%s" % id,
        "previewSize": "10"
    }

    response = requests.get(url, headers=headers, params=params)

    # totalCount 总件数
    data_totalCount = str(response.json()['result']['totalCount'])

    # totalPrice 总价值
    data_totalPrice = str(response.json()['result']['totalPrice'] / 100)

    # 再次访问详细库存
    headers_ = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Origin": "https://news.wmpvp.com",
        "Referer": "https://news.wmpvp.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.82",
        "X-Requested-With": "XMLHttpRequest",
        "appversion": "",
        "platform": "h5_web",
        "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "^\\^Android^^",
        "token": ""
    }
    url_ = "https://gwapi.pwesports.cn/appdecoration/steamcn/csgo/decoration/getSteamInventory"
    params_ = {
        "steamId": "%s" % id,
        "realTime": "0"
    }
    response = requests.get(url_, headers=headers_, params=params_)

    # 遍历饰品信息
    data = ''
    for i in range(0, int(data_totalCount)):
        # marketname 名称
        marketName = response.json()['result'][i]['marketName']

        # label 改名信息
        label = response.json()['result'][i]['label']
        if label == None:
            label = '无'
        else:
            label = label

        # suggestPrice 价格
        suggestPrice = response.json()['result'][i]['suggestPrice']
        if suggestPrice == 0:
            suggestPrice = '--'
        else:
            suggestPrice = str(suggestPrice / 100)

        # wearValue 磨损
        wearValue = response.json()['result'][i]['wearValue']
        if wearValue == None:
            wearValue = '--'
        else:
            wearValue = wearValue
        data = data + '名称：%s  改名：%s  价格：%s  磨损：%s\n' % (marketName, label, suggestPrice, wearValue)

    if int(data_totalCount) > 20:
        draw_txt(data)
        return '饰品总件数：%s  饰品总价值：%s' % (data_totalCount, data_totalPrice)
    else:
        return data

def hot_gun(id):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://news.wmpvp.com",
        "Referer": "https://news.wmpvp.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
        "X-Requested-With": "XMLHttpRequest",
        "accessToken": "",
        "appversion": "",
        "device": "undefined",
        "platform": "h5_web",
        "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }
    url = "https://api.wmpvp.com/api/v2/csgo/pvpDetailDataStats"

    data = '{"steamId64":"%s","csgoSeasonId":""}' % id

    response = requests.post(url, headers=headers, data=data)

    data = ''
    for i in range(0, 5):
        # weaponName 最擅长的武器
        data_weaponName = str(response.json()['data']['hotWeapons'][i]['weaponName'])

        # weaponKill 击杀数
        data_weaponKill = str(response.json()['data']['hotWeapons'][i]['weaponKill'])
        data = data + '\n' + '武器名：' + data_weaponName + '|击杀数：' + data_weaponKill
    return data

def hot_map(id):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Origin": "https://news.wmpvp.com",
        "Referer": "https://news.wmpvp.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.82",
        "X-Requested-With": "XMLHttpRequest",
        "appversion": "",
        "platform": "h5_web",
        "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "^\\^Android^^",
        "token": ""
    }
    url = "https://gwapi.pwesports.cn/appdatacenter/api/v2/csgo/pvpMapStats"
    params = {
        "steamId64": "%s" % id,
        "csgoSeasonId": "S11"
    }

    response = requests.get(url, headers=headers, params=params)

    result = ''
    for i in range(0, 3):
        # 地图名
        mapName = response.json()['result'][i]['mapNameZh']

        # 地图场次
        matchCnt = str(response.json()['result'][i]['matchCnt'])

        # 获胜场次
        winCnt = str(response.json()['result'][i]['winCnt'])

        # 胜率
        winRate = str(response.json()['result'][i]['winRate'] * 100) + "%"

        result = result + '\n' + '地图名：%s||地图场次：%s获胜场次：%s胜率：%s' % (mapName, matchCnt, winCnt, winRate)
    return result

async def get_(id):
    async with AioWebSocket('wss://wss-csgo-pwa.wmpvp.com/') as aws:
        converse = aws.manipulator
        message = '{"messageType":10001,"messageData":{"steam_id": "%s"}}' % id
        await converse.send(message)
        while True:
            mes = await converse.receive()
            try:
                string_mes = mes.decode('utf-8')  # 将字节数据转换为字符串数据

            except AttributeError as erro:
                pass
                # 状态码
                messageType = re.findall('"messageType":(.*?),', string_mes)[0]

                # 10003比赛结束
                # 10002正在进行

                if messageType == '10002':

                    # 开始时间
                    startTime = re.findall('"startTime":"(.*?)"', string_mes)[0]

                    # 进行时间
                    duration = re.findall('"duration":"(.*?)"', string_mes)[0]

                    # 地图
                    map = re.findall('"map":"(.*?)"', string_mes)[0]

                    # ctScore ct获胜局数
                    ctScore = re.findall('"ctScore":(.*?),', string_mes)[0]

                    # terroristScore t获胜局数
                    terroristScore = re.findall('"terroristScore":(.*?),', string_mes)[0]

                    json_mes = json.loads(string_mes)
                    for i in range(0, 9):
                        ID = json_mes['messageData']['playerList'][i]['steamId']

                        if ID == id:
                            # 所在阵营side
                            side = json_mes['messageData']['playerList'][i]['side']

                            # 击杀数kill
                            kill = json_mes['messageData']['playerList'][i]['kill']

                            # 爆头率headshot
                            headshot = json_mes['messageData']['playerList'][i]['headshot'] + '%'

                            # adr
                            adr = json_mes['messageData']['playerList'][i]['adr']

                            # death死亡数
                            death = json_mes['messageData']['playerList'][i]['death']

                            # assist助攻
                            assist = json_mes['messageData']['playerList'][i]['assist']

                            # score得分
                            score = json_mes['messageData']['playerList'][i]['score']

                            return '对局正在进行中！\n开始时间：{}\n已经进行：{}分钟\n地图：{}\nCT阵营分数：{}\nT阵营分数:{}\n所在阵营：{}\n击杀数：{}\n爆头率：{}\nAADR：{}\n死亡数：{}\n助攻：{}\n得分：{}'.format(
                                startTime, duration, map, ctScore, terroristScore, side, kill, headshot, adr, death,
                                assist, score)
                else:
                    return '没有正在进行的对局！'
            # aws.close_connection()

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
    return info + '数据仅参考，购买需谨慎'

def elo_img(id):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://news.wmpvp.com",
        "Referer": "https://news.wmpvp.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
        "X-Requested-With": "XMLHttpRequest",
        "accessToken": "",
        "appversion": "",
        "device": "undefined",
        "platform": "h5_web",
        "sec-ch-ua": "^\\^Not.A/Brand^^;v=^\\^8^^, ^\\^Chromium^^;v=^\\^114^^, ^\\^Microsoft",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^"
    }
    url = "https://api.wmpvp.com/api/v2/csgo/pvpDetailDataStats"

    data = '{"steamId64":"%s","csgoSeasonId":""}' % id

    response = requests.post(url, headers=headers, data=data)

    data_historyScores = []

    for i in range(0, 10):
        historyScores = response.json()['data']['historyScores'][i]

        data_historyScores.append(historyScores)

        # 示例数据
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = data_historyScores[::-1]  # 切片反转数组

    # 创建趋势图
    fig = go.Figure()

    # 添加线条
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=''))

    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='markers+text',
        text=y,
        name='',
        textposition="top center",
        textfont=dict(color='black'),
        marker=dict(size=10, color='red')
    ))

    # 隐藏图例
    fig.update_layout(showlegend=False)

    # 设置布局
    fig.update_layout(
        title={
            'text': '近10场ELO趋势图',
            'x': 0.5,  # 将标题水平位置设置为0.5，即图表中心
        },
        xaxis_showgrid=False,  # 显示 x 轴的横向表格
        yaxis_showgrid=True,  # 隐藏 y 轴的纵向表格
        xaxis_gridcolor='white',  # 将纵向表格背景色设为白色
        xaxis=dict(
            tickmode='linear',  # 刻度显示方式为线性
            dtick=1,  # 刻度间隔为1
            ticklen=20,  # 延长刻度线长度为20
            showline=True,  # 显示 x 轴表格边缘
            linecolor='black'  # 将 x 轴表格边缘设为黑色
        ),
        yaxis=dict(
            showline=True,  # 显示 y 轴表格边缘
            linecolor='black'  # 将 y 轴表格边缘设为黑色
        )
    )

    # 显示图表
    fig.show()
    return 'success'

def draw_txt(text):
    font_path = "simsun.ttc"  # 字体文件路径
    font_size = 20  # 字体大小

    def draw_text_with_constraint(text, font_path, font_size):
        # 计算文本所占的空间
        lines = text.split('\n')
        max_line_width = max([ImageFont.truetype(font_path, font_size).getbbox(line)[2] for line in lines])
        total_height = sum([ImageFont.truetype(font_path, font_size).getbbox(line)[3] + 10 for line in lines])

        # 设置图片尺寸
        image_width = max_line_width + 40 + 100
        image_height = total_height + 40 + 50

        # 创建空白图片
        image = Image.open('index_bk.jpg')

        image = image.resize((image_width, image_height))

        draw = ImageDraw.Draw(image)

        # 加载字体
        font = ImageFont.truetype(font_path, font_size)

        # 设置文字位置和边距
        margin_left = 20
        margin_top = 20

        # 绘制文本
        y = margin_top
        for line in lines:
            draw.text((margin_left, y), line, font=font, fill='white')
            y += font.getbbox(line)[3] + 10

        return image

    image = draw_text_with_constraint(text, font_path, font_size)
    image.save('draw_Money.png')

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
        url = 'https://arena.5eplay.com/api/search?keywords=%s' % name
        url = urllib.parse.quote(url, safe=string.printable)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}
        requst = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(requst)
        jsdata = json.loads(response.read().decode("utf-8"))
        try:
            eid = jsdata['data']['user']['list'][0]['domain']
        except IndexError:
            return 'erro'

        def w2_decrypt(arg):
            with open("./ws_.js") as f:  # 调用js文件
                jsdata = f.read()
                ctx = execjs.compile(jsdata)
                data = ctx.call('l', '%s' % arg)
                # print(data)
            return data

        url = 'https://arena.5eplay.com/data/player/%s' % eid
        # print(url)
        # gzip压缩网页解决方法
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}
        req = get(url)
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
            url = 'https://arena.5eplay.com/data/player/%s' % eid
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
                'cookie': 'acw_sc__v2=' + w2}
            req = urllib.request.Request(url, headers=headers)
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

            def get_height():  # 高光mp4
                for url in get_item():
                    req = urllib.request.Request(url, headers=headers)
                    result = urllib.request.urlopen(req)
                    result = result.read().decode('utf-8')
                    data = re.findall(findHeight, result)
                return data

            try:
                data = get_val(), get_pie(), get_desc()[0], get_clearfix(), get_img(), get_height()

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
        return '未找到对应的ID，请检查你的用户名是否正确！'
    else:
        data = '总排名：{}\n总比赛：{}\n贡献值RWS：{}\n技术得分Rating：{}\n天梯：{}\n游戏时长：{}\n平均每局杀敌：{}\n平均每局助攻：{}\n每局存活率：{}\n' \
               'MPV：{}\nK/D：{}\n爆头率：{}\n胜率：{}\n{}{}\n1V5：{}\n1V4：{}\n1V3：{}\n5K：{}\n4K：{}\n3K：{}\n'
        try:
            result = data.format(*list)
            return list
        except TypeError:
            return '您当前未完成定级赛，完成定级赛后才可查看战绩'

