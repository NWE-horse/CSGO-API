# -*- codeing = utf-8 -*-
# @Time : 2023/8/8 19:30
# @Author :Jnine
# @File : utils.py
# @Software : PyCharm

from PIL import Image, ImageDraw, ImageFont
import yaml
import json

def _draw_txt(text: str) -> None:
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

    image = draw_text_with_constraint(text, font_path, font_size)
    image.save('draw_Money.png')

def get_config():
    with open('./config.yml', 'r',encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config

def get_api(field:str) -> json:
    with open('data/api.json') as f:
        data = json.loads(f.read())[field]
        return data