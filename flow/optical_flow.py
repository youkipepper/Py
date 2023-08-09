# import cv2
# import numpy as np

# # 定义函数：计算局部相位和局部振幅
# def calculate_phase_amplitude(frame):
#     # 在此处进行局部相位和局部振幅的计算
#     phase = np.angle(np.fft.fftshift(np.fft.fft2(frame)))
#     amplitude = np.abs(np.fft.fftshift(np.fft.fft2(frame)))
#     return phase, amplitude

# # 定义函数：根据局部相位计算图像速度
# def calculate_velocity(phase):
#     phase_diff_x = np.diff(phase, axis=1)
#     non_zero_mask = phase_diff_x != 0
#     velocity_x = np.where(non_zero_mask, 1 / phase_diff_x, 1e-9)
#     return velocity_x


# # 定义函数：将运动信号应用于图像序列
# def apply_motion_signal(frame, velocity):
#     amplified_frame = np.roll(frame, velocity.flatten().astype(int), axis=1)
#     return amplified_frame


# # 读取视频文件
# video_path = 'input_video.mp4'
# cap = cv2.VideoCapture(video_path)

# # 定义需要人为设定的参数
# downsampling_level = 4
# edge_detection_threshold = 100  # 边缘检测的阈值
# epsilon = 0.1  # 用于计算频带的参数

# # 定义保存视频的参数
# output_video_path = 'output_amplified_video.mp4'
# fps = 30  # 帧率
# frame_size = (int(cap.get(3)), int(cap.get(4)))  # 使用原始视频的帧大小

# # 创建VideoWriter对象
# # fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 使用XVID编码
# fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')  # 使用MJPG编码
# out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

# # 处理每一帧视频
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     # 图像预处理：下采样和边缘检测
#     resized_frame = cv2.resize(frame, None, fx=1/downsampling_level, fy=1/downsampling_level)
#     gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gray_frame, edge_detection_threshold, edge_detection_threshold*2)
    
#     # 计算局部相位和局部振幅
#     phase, amplitude = calculate_phase_amplitude(edges)
    
#     # 根据局部相位计算图像速度
#     velocity = calculate_velocity(phase)
    
#     # 将运动信号应用于图像序列，生成放大效果的图像
#     amplified_frame = apply_motion_signal(frame, velocity)
    
#     # 将放大效果的帧写入保存视频
#     out.write(amplified_frame)
    
#     # 显示放大效果的图像
#     cv2.imshow('Amplified Video', amplified_frame)
    
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         break

# # 释放VideoWriter对象
# out.release()

# cap.release()
# cv2.destroyAllWindows()



import cv2
import numpy as np

# 定义函数：计算局部相位和局部振幅
def calculate_phase_amplitude(frame):
    # 在此处进行局部相位和局部振幅的计算
    phase = np.angle(np.fft.fftshift(np.fft.fft2(frame)))
    amplitude = np.abs(np.fft.fftshift(np.fft.fft2(frame)))
    return phase, amplitude

# 定义函数：根据局部相位计算图像速度
def calculate_velocity(phase):
    phase_diff_x = np.diff(phase, axis=1)
    non_zero_mask = phase_diff_x != 0
    velocity_x = np.where(non_zero_mask, 1 / phase_diff_x, 1e-9)
    return velocity_x

# 定义函数：将运动信号应用于图像序列
def apply_motion_signal(frame, velocity):
    amplified_frame = np.roll(frame, velocity.flatten().astype(int), axis=1)
    return amplified_frame

# 读取视频文件
video_path = 'input_video.mp4'
cap = cv2.VideoCapture(video_path)

# 定义需要人为设定的参数
edge_detection_threshold = 100

# 定义保存视频的参数
output_video_path = 'output_amplified_video.mp4'
fps = 30

# 获取视频的帧大小
frame_size = (int(cap.get(3)), int(cap.get(4)))

# 创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 边缘检测
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_frame, edge_detection_threshold, edge_detection_threshold * 2)

    # 计算局部相位和局部振幅
    phase, amplitude = calculate_phase_amplitude(edges)

    # 根据局部相位计算图像速度
    velocity = calculate_velocity(phase)

    # 将运动信号应用于图像序列，生成放大效果的图像
    amplified_frame = apply_motion_signal(frame, velocity)

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
