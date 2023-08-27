import cv2
import numpy as np
import matplotlib.pyplot as plt

def preprocess_image(image):
    # 高斯金字塔下采样
    downsampled_image = cv2.pyrDown(image)
    return downsampled_image

def generate_edge_mask(image):
    # 提取幅度
    fft_image = np.fft.fft2(image)
    amplitude = np.abs(fft_image)
    
    # 设置幅度阈值，根据需要进行调整
    threshold = 1000
    
    # 生成边缘掩模
    edge_mask = (amplitude > threshold).astype(np.uint8)
    
    return edge_mask

def apply_phase_based_optical_flow(image, edge_mask):
    # 对掩模中的活动像素应用相位法光流
    flow = cv2.calcOpticalFlowFarneback(image, image, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    active_pixels = flow[edge_mask == 1]
    
    return active_pixels

def calculate_velocity(phase, dx, dy, dt):
    # 计算像素单位的速度
    vx = (np.gradient(phase, dx, axis=0) / dt).flatten()
    vy = (np.gradient(phase, dy, axis=1) / dt).flatten()
    
    return vx, vy

# 读取图像
image_path = 'path_to_your_image.jpg'  # 替换为你的图像路径
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 图像预处理
preprocessed_image = preprocess_image(image)

# 生成边缘掩模
edge_mask = generate_edge_mask(preprocessed_image)

# 应用相位法光流
active_pixels = apply_phase_based_optical_flow(preprocessed_image, edge_mask)

# 计算像素单位的速度
dx = dy = 1  # 像素尺寸
dt = 1      # 时间间隔
vx, vy = calculate_velocity(active_pixels, dx, dy, dt)

# 将像素速度转换为实际尺度（例如，毫米）
scaling_factor = 0.1  # 适当的缩放因子，根据需要进行调整
vx_mm = vx * scaling_factor
vy_mm = vy * scaling_factor

# 显示原始图像、下采样图像和提取的边缘掩模
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(132)
plt.imshow(preprocessed_image, cmap='gray')
plt.title('Downsampled Image')

plt.subplot(133)
plt.scatter(vx_mm, vy_mm, s=1)
plt.xlabel('X Velocity (mm/s)')
plt.ylabel('Y Velocity (mm/s)')
plt.title('Pixel Velocities')

plt.tight_layout()
plt.show()
