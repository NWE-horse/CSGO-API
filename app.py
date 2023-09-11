from flask import Flask
import asyncio
import matter_function

app = Flask(__name__)
from data import utils
import webbrowser
config = utils.get_config()

html_file = 'Api_Documentation.html'
@app.route('/video/<id>')
def video(id):
    return matter_function.video(id)


@app.route('/personal_info_wanmei/<id>')
def personal_info_wanmei(id):
    return matter_function.info_wm(id)


@app.route('/guns_money/<id>')
def guns_money(id):
    return matter_function.guns_money(id)


@app.route('/hot_gun/<id>')
def hot_gun(id):
    return matter_function.hot_gun(id)


@app.route('/hot_maps/<id>')
def hot_maps(id):
    return matter_function.hot_map(id)


@app.route('/watch_game/<id>')
def watch_game(id):
    return asyncio.run(matter_function.game_play(id))


@app.route('/trade_ie/<id>')
def guns_ie(id):
    return matter_function.gun_ie(id)


# @app.route('/elo_img/<id>')
# def elo_img(id):
#     return matter_function.elo_img(id)


@app.route('/personal_info_5E/<id>')
def personal_info_5e(id):
    return matter_function.data_5e(id)


# @app.route('/bilibili_dynamic')
# def bilibili_dynamic():
#     # 创建子线程
#     # thread = threading.Thread(target=matter_function.bilibili_dynamic)
#     return matter_function.bilibili_dynamic()


@app.route('/player_ranking')
def player_ranking():
    return matter_function.player_ranking()


@app.route('/team_ranking')
def team_ranking():
    return matter_function.team_ranking()

@app.route('/boxlucky')
def boxLucky():
    return matter_function.boxLucky()

@app.route('/matchlist')
def matchlist():
    return matter_function.match()

if __name__ == '__main__':
    webbrowser.open(html_file)
    app.run(port=config['port'],host=config['host'])


