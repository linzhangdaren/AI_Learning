#这是一个可以在cv中显示中文字的模块
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def cv2AddChineseText(img, text, position, textColor=(0, 255, 0), textSize=30):
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    print(type(img))
    draw = ImageDraw.Draw(img)
    
    # 字体的格式
    fontStyle = ImageFont.truetype("C:/Windows/Fonts/msyh.ttc", textSize, encoding="utf-8")
    
    # 绘制文本
    draw.text(position, text, textColor, font=fontStyle)
    
    # 转换回OpenCV格式
    return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)