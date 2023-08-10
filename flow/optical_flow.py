import cv2
import numpy as np

# 读取视频文件
video_path = 'input_video.mp4'
cap = cv2.VideoCapture(video_path)

# 定义阈值和放大因子
amplitude_threshold = 100  # 高幅值阈值
amplification_factor = 5.0  # 放大因子

# 创建VideoWriter对象
output_video_path = 'output_amplified_video.mp4'
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

# 处理每一帧视频
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 进行傅立叶变换
    frequency_matrix = np.fft.fft2(frame)
    
    # 提取高幅值区域
    amplitude = np.abs(frequency_matrix)
    high_amplitude_mask = amplitude > amplitude_threshold
    high_amplitude_frequency = frequency_matrix * high_amplitude_mask
    
    # 对高幅值区域进行放大操作
    amplified_high_amplitude_frequency = high_amplitude_frequency * amplification_factor
    
    # 重构频域复数矩阵
    amplified_frequency_matrix = frequency_matrix + (amplified_high_amplitude_frequency - high_amplitude_frequency)
    
    # 进行逆傅立叶变换
    amplified_frame = np.fft.ifft2(amplified_frequency_matrix).real.astype(np.uint8)
    
    # 将放大效果的帧写入保存视频
    out.write(amplified_frame)
    
    # 显示放大效果的图像
    cv2.imshow('Amplified Video', amplified_frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 释放VideoWriter对象
out.release()

cap.release()
cv2.destroyAllWindows()
