# OpenCV读取摄像头视频流获取摄像机
import cv2
import numpy as np
import time
#导入自定义的模块 显示中文汉字的函数
import drawUtils

# 读取摄像头
cap = cv2.VideoCapture(0)

#计算帧率
#当前Unix时间戳
start_time = time.time()
#计数器


#循环读取视频帧
while True:
    rec,frame=cap.read()
    #rec表示是否成功读取到视频帧
    #frame表示当前帧的图像 存储为一个numpy.ndarray数组
    
    #镜像翻转画面
    frame=cv2.flip(frame,1)
    
    #作画/////////////////////
    #画矩形
    cv2.rectangle(frame,(100,100),(300,300),(0,255,0),2)
    
    #帧率计算方法
    now=time.time()
    fps_text=int(1/(now-start_time))
    start_time=now#更新起始时间
    # print(fps_text)#查看帧率
    frame_text="帧率:"+str(fps_text)
    
    #显示帧率到画面frame_text包含中文字符用自定义的函数显示
    frame=drawUtils.cv2AddChineseText(frame, frame_text, (10, 10), textColor=(255, 255, 255), textSize=20)
    #/////////////////////
    
    #显示当前画面
    cv2.imshow("Demo",frame)
    
    #退出条件
    if cv2.waitKey(1) & 0xFF == 27:#q退出或着键Esc退出 0xFF == 27
        break 
    
#释放cap对象
cap.release()
#销毁所有窗口
cv2.destroyAllWindows()