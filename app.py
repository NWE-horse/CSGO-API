from flask import Flask
import asyncio
import matter_function
import threading
app = Flask(__name__)


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
    return asyncio.run(matter_function.get_(id))


@app.route('/trade_ie/<id>')
def guns_ie(id):
    return matter_function.gun_ie(id)


@app.route('/elo_img/<id>')
def elo_img(id):
    return matter_function.elo_img(id)


@app.route('/personal_info_5E/<id>')
def personal_info_5E(id):
    return matter_function.data_5E(id)


@app.route('/bilibili_dynamic')
def bilibili_dynamic():
    # 创建子线程
    thread = threading.Thread(target=matter_function.bilibili_dynamic)
    thread.start()
    return {"code":'1',
            "message":'success'}


if __name__ == '__main__':
    app.run()
