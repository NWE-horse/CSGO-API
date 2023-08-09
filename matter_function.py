# -*- codeing = utf-8 -*-
# @Time : 2023/7/31 21:19
# @Author :Jnine
# @File : Matter_class.py
# @Software : PyCharm
from datetime import datetime
import urllib
import string
import bs4
import urllib.request
import json
import plotly.graph_objects as go
from urllib import parse
import requests
from aiowebsocket.converses import AioWebSocket
import re
import csgoapi


def data_5e(name):
    return csgoapi.five_e.data_5E(name)


def info_wm(id):
   return csgoapi.wanmei.info_wm(id)


def video(id):
    return csgoapi.wanmei.video()


def guns_money(id):
    return csgoapi.wanmei.guns_money(id)


def hot_gun(id):
    return csgoapi.wanmei.hot_gun(id)


def hot_map(id):
    return csgoapi.wanmei.hot_map(id)


async def game_play(id):
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
    return csgoapi.trading.gun_ie(name)


def boxLucky():
   return csgoapi.wanmei.boxLucky()


def match():
    return csgoapi.wanmei.match()
