# OpenCV读取摄像头视频流获取摄像机
import cv2
import numpy as np


# 读取摄像头
cap = cv2.VideoCapture(0)

#保存视频流为mp4文件 视频大小可以自定义不用获取
save_patch=('D:/Desktop/video.mp4')#视频保存路径
fourcc = cv2.VideoWriter_fourcc(*'mp4v')#编码器
fps=30#帧率
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#获取摄像头源视频宽度
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#获取摄像头源视频高度
#写入参数到writer
writer=cv2.VideoWriter(save_patch,fourcc,fps,(width,height))

#循环读取视频帧
while True:
    rec,frame=cap.read()
    #rec表示是否成功读取到视频帧
    #frame表示当前帧的图像 存储为一个numpy.ndarray数组
    
    #镜像翻转
    frame=cv2.flip(frame,1)
    # #灰度显示
    # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #写入writer 写入画面到文件
    writer.write(frame)
    
    #显示当前画面
    cv2.imshow("camera",frame)
    
    #退出条件
    if cv2.waitKey(1) & 0xFF == ord('q'):#q退出或着键Esc退出 0xFF == 27
        break 
    
#释放writer
writer.release()    
#释放摄像头
cap.release()
#销毁所有窗口
cv2.destroyAllWindows()