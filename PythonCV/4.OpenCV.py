# 在python中使用OpenCV
import cv2
import numpy as np
import os

# 切换工作目录到当前脚本所在目录
os.chdir(os.path.dirname(__file__))

# 读取照片
img = cv2.imread("img/guishu.jpg")

while True:
    # 显示图片
    cv2.imshow("Demo", img)  # "Demo"为窗口名，img是要显示的图片
    # 退出条件
    # 每一毫秒检测是否有ESC(27)按键输入，如果有就退出
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 释放所有窗口
cv2.destroyAllWindows()
