import cv2

# 打开摄像头并读取视频流
cap = cv2.VideoCapture(0)

while True:
    # 从视频流中读取帧
    ret, frame = cap.read()

    # 如果成功读取到帧
    if ret:
        # 在窗口中显示帧
        cv2.imshow('Video', frame)

    # 检测按下 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭所有窗口
cv2.destroyAllWindows()
