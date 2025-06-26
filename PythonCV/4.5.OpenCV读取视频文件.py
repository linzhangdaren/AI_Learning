# OpenCV读取视频文件
import cv2
import numpy as np
import time

# 将要读取的视频文件路径
save_patch=('D:/Desktop/video.mp4')
# 读取文件
cap = cv2.VideoCapture(save_patch)
#如果打不开提示编码或着找不到文件
if not cap.isOpened():
    print("编码错误或着找不到此文件请检查路径")
    
#循环读取视频帧///////////////////////////////////
while cap.isOpened():
    ret, frame = cap.read()#解包
    if ret:#当读完帧会变为0 就会跳到else
        #显示当前帧画面
        cv2.imshow("camera", frame)
        #延时1ms(播放速率的控制,不加默认读取太快了)
        time.sleep(0.033)
        #播放中途可以按q退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:#播放完毕自动退出
        break
#///////////////////////////////////////////////   

#释放cap对象
cap.release()
#销毁所有窗口
cv2.destroyAllWindows()