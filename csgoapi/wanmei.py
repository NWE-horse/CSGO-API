# -*- codeing = utf-8 -*-
# @Author :Jnine
# @File : wanmei.py
# @Software : PyCharm
import requests
from aiowebsocket.converses import AioWebSocket
import json

from data import utils
from datetime import datetime
import re

headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.82",
    }
config = utils.get_config()
API = utils.get_api('wanmei')

def guns_money(id: str) -> str:
    params = {
        "steamId": f"{id}",
        "previewSize": "10"
    }
    response = requests.get(API['getSteamInventoryPreview'], headers=headers, params=params)

    # totalCount 总件数
    data_totalCount = str(response.json()['result']['totalCount'])

    # 详细库存
    params = {
        "steamId": f"{id}",
    }
    response = requests.get(API['getSteamInventory'], headers=headers, params=params)

    if config['original'] == False:
        data = ''

        for i in range(0, int(data_totalCount)):
            # marketname 名称
            marketName = response.json()['result'][i]['marketName']

            # label 改名信息
            label = response.json()['result'][i]['label']
            if label == None:
                label = '-'
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
            data += f'名称：{marketName}  改名：{label}  价格：{suggestPrice}  磨损：{wearValue}\n'

        return data
    else:
        return response.json()

def hot_gun(id: str) -> str:
    #特殊请求头
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
        "device": "undefined",
        "platform": "h5_web",
    }
    params = '{"steamId64":"%s","csgoSeasonId":""}' % id

    response = requests.post(API['pvpDetailDataStats'], headers=headers, data=params)

    if config['original'] == False:
        data = ''
        for i in range(len(response.json()['data']['hotWeapons'])):
            # weaponName 最擅长的武器
            data_weaponName = str(response.json()['data']['hotWeapons'][i]['weaponName'])

            # weaponKill 击杀数
            data_weaponKill = str(response.json()['data']['hotWeapons'][i]['weaponKill'])

            head_weaponKill = str(response.json()['data']['hotWeapons'][i]['weaponHeadShot'])

            data += f'\n' + f'武器名：【{data_weaponName}】 击杀数：{data_weaponKill}  爆头数{head_weaponKill}  爆头率：{round(round(int(head_weaponKill) / int(data_weaponKill), 4) * 100, 2)}%'
        return data
    else:
        return response.json()

def hot_map(id: str) -> str:
    params = {
        "steamId64": "%s" % id,
        "csgoSeasonId": "S12"
    }

    response = requests.get(API['pvpMapStats'], headers=headers, params=params)

    if config['original'] == False:
        result = ''
        for i in range(len(response.json()['result'])):
            # 地图名
            mapName = response.json()['result'][i]['mapNameZh']

            # 地图场次
            matchCnt = str(response.json()['result'][i]['matchCnt'])

            # 获胜场次
            winCnt = str(response.json()['result'][i]['winCnt'])

            # 胜率
            winRate = str(round(response.json()['result'][i]['winRate'] * 100,1))

            result += f'【地图名：{mapName}】地图场次：{matchCnt} 获胜场次：{winCnt} 胜率：{winRate}%\n'

        return result
    else:
        return response.json()

def info_wm(id: str) -> str:
    # 特殊请求头
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82",
        "device": "undefined",
        "platform": "h5_web",
    }

    data = '{"steamId64":"%s","csgoSeasonId":""}' % id

    response = requests.post(API['pvpDetailDataStats'], headers=headers, data=data)

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
    if config['original'] == False:
        data_result = f'游戏名：{data_name}\n天梯分数：{data_elo}\n场次：{data_cnt}\nKD：{data_kd}\n' \
                      f'胜率：{data_winRate}\nrating：{data_rating}\n总击杀：{data_kills}\n总助攻：{data_assists}\n' \
                      f'总死亡：{data_deaths}\nmvp次数：{data_mvpCount}\nrws：{data_rws}\nadr：{data_adr}\n' \
                      f'爆头率：{data_headShotRatio}\n首杀率：{data_entryKillRatio}\n你的评价是：{data_summary}\navatar:{data_avatar}'
        return data_result
    else:
        return response.json()

def video(id: str) -> str:

    params = {
        "toSteamId": id,
    }

    response = requests.get(API['getPerfectList'], headers=headers, params=params)
    if config['original'] == False:
        title = response.json()['result']['userVideoList'][0]['title']

        videoURL = response.json()['result']['userVideoList'][0]['videoInfo']['playInfoList'][0]['playURL']

        return title + videoURL
    else:
        return response.json()

def match():
    params = {
        "matchTime": f"{datetime.now().strftime('%Y-%m-%d')} 00:00:00"
    }
    response = requests.get(API['getMatchList'], headers=headers, params=params)

    list = response.json()['result']['matchResponse']['dtoList']

    if config['original']:
        data = ''
        for i in range(5):
            name = list[i]['csgoEventDTO']['nameZh']

            team1 = list[i]['team1DTO']['name']

            team2 = list[i]['team2DTO']['name']

            score1 = list[i]['score1']

            score2 = list[i]['score2']

            bo = list[i]['bo']

            winnerTeamId = list[i]['winnerTeamId']

            start_time = datetime.fromtimestamp(list[i]['startTime'] / 1000)

            state = ''
            if score1 == None:
                score1 = '0'
            if score2 == None:
                score2 = '0'
            if start_time > datetime.now():
                state = '【未开始】'
            if winnerTeamId != None:
                state = '【已结束】'
            elif start_time < datetime.now() and winnerTeamId == None:
                state = '【进行中】'

            data += f'{name}\n开始时间：{start_time.strftime("%H:%M:%S")}\n{team1}[{score1}:{score2}]{team2}{state}\n'
        return data
    else:
        return response.json()

def boxLucky():
    response = requests.get(API['getLuckyHitInfoStation'], headers=headers)

    list = response.json()['result']['boxLuckyRank']['list']
    if config['original'] == False:
        data = ''

        for i in range(len(list)):
            boxname = list[i]['boxName']
            luckyrate = list[i]['luckyRate']
            data += boxname + luckyrate + '\n'
        return data
    else:
        return response.json()

async def game_play(id):
    async with AioWebSocket(API['gameplay']) as aws:
        converse = aws.manipulator
        message = '{"messageType":10001,"messageData":{"steam_id": "%s"}}' % id
        await converse.send(message)
        while True:
            mes = await converse.receive()
            if config['original'] == False:
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
            else:
                return mes
            # aws.close_connection()