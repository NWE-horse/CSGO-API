from flask import Flask
import asyncio
import Matter_class

app = Flask(__name__)


@app.route('/vedio/<id>')
def vedio(id):
    return Matter_class.video(id)


@app.route('/perseonal_info_wanmei/<id>')
def perseonal_info_wanmei(id):
    return Matter_class.info_wm(id)


@app.route('/guns_money/<id>')
def guns_money(id):
    return Matter_class.guns_money(id)


@app.route('/hot_gun/<id>')
def hot_gun(id):
    return Matter_class.hot_gun(id)


@app.route('/hot_maps/<id>')
def hot_maps(id):
    return Matter_class.hot_map(id)


@app.route('/watch_game/<id>')
def watch_game(id):
    return asyncio.run(Matter_class.get_(id))


@app.route('/guns_ie/<id>')
def guns_ie(id):
    return Matter_class.gun_ie(id)


@app.route('/elo_img/<id>')
def elo_img(id):
    return Matter_class.elo_img(id)


@app.route('/perseonal_info_5E/<id>')
def perseonal_info_5E(id):
    return Matter_class.data_5E(id)


if __name__ == '__main__':
    app.run()
