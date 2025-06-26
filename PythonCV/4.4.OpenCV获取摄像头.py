# OpenCV读取摄像头视频流获取摄像机
import cv2
import numpy as np


# 读取摄像头
cap = cv2.VideoCapture(0)

#循环读取视频帧
while True:
    rec,frame=cap.read()
    #rec表示是否成功读取到视频帧
    #frame表示当前帧的图像 存储为一个numpy.ndarray数组
    
    #镜像翻转
    frame=cv2.flip(frame,1)
    #灰度显示
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #显示当前画面
    cv2.imshow("camera",frame)
    
    #退出条件
    if cv2.waitKey(1) & 0xFF == ord('q'):#q退出或着键Esc退出 0xFF == 27
        break 
    
#释放摄像头
cap.release()
#销毁所有窗口
cv2.destroyAllWindows()