import cv2
import numpy as np
from scipy.ndimage import convolve

# 加载输入视频
input_video_path = 'input_video.mp4'
cap = cv2.VideoCapture(input_video_path)

# 设置输出视频文件名和参数
output_video_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # 使用其他编解码器，如'MJPG'或'MP4V'
frame_size = (int(cap.get(3)), int(cap.get(4)))
fps = int(cap.get(5))

# 创建输出视频对象
out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)

# 高斯金字塔和边缘掩码生成的参数
num_levels = 4
threshold = 50

# 对原始图像序列应用高斯金字塔以减少白噪声
def generate_pyramid_frames(frames):
    pyramid_frames = [cv2.pyrDown(frame) for frame in frames]
    return pyramid_frames

# 使用相位法光流生成的振幅来生成边缘掩码
def generate_edge_mask(frames, threshold):
    edge_mask = []
    
    for i in range(1, len(frames)):
        prev_frame = cv2.cvtColor(frames[i-1], cv2.COLOR_BGR2GRAY)
        curr_frame = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
        
        flow = cv2.calcOpticalFlowFarneback(prev_frame, curr_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        amplitude = np.sqrt(flow[..., 0]**2 + flow[..., 1]**2)
        
        edge_mask.append(amplitude > threshold)
    
    return edge_mask

# 计算相位法光流
def calculate_optical_flow(prev_frame, curr_frame):
    flow = cv2.calcOpticalFlowFarneback(prev_frame, curr_frame, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    return flow

# 使用边缘掩码对每一帧应用相位法光流
def apply_motion_magnification(frames, edge_mask, amplification_factor, fps):
    amplified_frames = []
    
    for i, frame in enumerate(frames):
        if i == 0:
            prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            continue
        
        curr_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        flow = calculate_optical_flow(prev_frame, curr_frame)
        
        flow_masked = flow * edge_mask[i-1][..., np.newaxis]
        local_phase = np.arctan2(flow_masked[..., 1], flow_masked[..., 0])
        local_amplitude = np.sqrt(flow_masked[..., 0]**2 + flow_masked[..., 1]**2)
        
        kernel = np.ones((3, 3)) / 9
        motion_signals_blurred = convolve(local_amplitude, kernel, mode='constant', cval=0.0)
        
        motion_signals_filtered = cv2.GaussianBlur(motion_signals_blurred, (0, 0), 2)
        
        fft_freqs = np.fft.fftshift(np.fft.fftfreq(local_phase.shape[0], d=1.0/fps))
        fft = np.fft.fftshift(np.fft.fft(local_phase, axis=0), axes=0)
        
        epsilon = 0.5  # 可根据需要调整
        lower_bound, upper_bound = np.min(fft_freqs), np.max(fft_freqs)
        
        amplified_signal = fft.copy()
        amplified_signal[(fft_freqs < lower_bound) | (fft_freqs > upper_bound)] = 0
        amplified_signal[(fft_freqs >= lower_bound) & (fft_freqs <= upper_bound)] *= amplification_factor
        
        amplified_phase = np.fft.ifft(np.fft.ifftshift(amplified_signal), axis=0)
        
        amplified_frame = np.zeros_like(frame)
        for channel in range(3):
            amplified_frame[..., channel] = curr_frame + amplified_phase.real
        
        amplified_frame = np.clip(amplified_frame, 0, 255).astype(np.uint8)
        amplified_frames.append(amplified_frame)
        prev_frame = curr_frame
    
    return amplified_frames

# 读取输入视频的帧
frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# 生成高斯金字塔和边缘掩码
pyramid_frames = generate_pyramid_frames(frames)
edge_mask = generate_edge_mask(pyramid_frames, threshold)

# 运动放大并保存输出视频
amplification_factor = 10
amplified_frames = apply_motion_magnification(pyramid_frames, edge_mask, amplification_factor, fps)

for frame in amplified_frames:
    out.write(frame)

out.release()
