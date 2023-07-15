import numpy as np
import matplotlib.pyplot as plt

# 系统参数
m1 = 1000  # 结构物1质量 (kg)
m2 = 2000  # 结构物2质量 (kg)
k1 = 10000  # 结构物1刚度 (N/m)
k2 = 20000  # 结构物2刚度 (N/m)
k12 = 15000  # 结构物1和结构物2之间的刚度 (N/m)
c = 500  # 结构物阻尼 (Ns/m)

m_tmd = 500  # TMD质量 (kg)
k_tmd = 15000  # TMD刚度 (N/m)
c_tmd = 200  # TMD阻尼 (Ns/m)

# 控制参数
k_c = 5000  # 控制增益

# 时间参数
t_start = 0  # 起始时间
t_end = 10  # 结束时间
dt = 0.01  # 时间步长

# 初始化变量
num_steps = int((t_end - t_start) / dt) + 1  # 时间步数
t = np.linspace(t_start, t_end, num_steps)  # 时间数组
x1 = np.zeros(num_steps)  # 结构物1的位移
x1_dot = np.zeros(num_steps)  # 结构物1的速度
x2 = np.zeros(num_steps)  # 结构物2的位移
x2_dot = np.zeros(num_steps)  # 结构物2的速度
y = np.zeros(num_steps)  # TMD的位移
y_dot = np.zeros(num_steps)  # TMD的速度

# 控制力数组
F_control = np.zeros(num_steps)

# 定义正弦激励参数
A = 0.1  # 振幅 (m)
f = 1.0  # 频率 (Hz)
phi = np.pi / 4  # 相位 (rad)

# 计算外部激励力
F1_ext = A * np.sin(2 * np.pi * f * t + phi)

# 迭代计算
for i in range(num_steps - 1):
    # 计算结构物1和2的加速度
    x1_acc = (F1_ext[i] - c * x1_dot[i] - k1 * x1[i] - k12 * (x1[i] - x2[i]) - k_tmd * (x1[i] - y[i])) / m1
    x2_acc = (k12 * (x1[i] - x2[i])) / m2
    
    # 计算TMD的加速度
    y_acc = (k_tmd * (x1[i] - y[i]) - c_tmd * y_dot[i] - m_tmd * y_dot[i] - F_control[i]) / m_tmd
    
    # 更新结构物1和2的位移和速度
    x1[i + 1] = x1[i] + x1_dot[i] * dt
    x1_dot[i + 1] = x1_dot[i] + x1_acc * dt
    x2[i + 1] = x2[i] + x2_dot[i] * dt
    x2_dot[i + 1] = x2_dot[i] + x2_acc * dt
    
    # 更新TMD的位移和速度
    y[i + 1] = y[i] + y_dot[i] * dt
    y_dot[i + 1] = y_dot[i] + y_acc * dt
    
    # 计算控制力
    F_control[i + 1] = -k_c * (x1[i + 1] - y[i + 1])

# 计算性能指标
x1_amplitude = np.max(np.abs(x1))  # 结构物1的振幅
y_amplitude = np.max(np.abs(y))  # TMD的振幅
damping_ratio = x1_amplitude / y_amplitude  # 减震比


# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(t, x1, label='Structure 1')
plt.plot(t, x2, label='Structure 2')
plt.plot(t, y, label='TMD')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('TMD Vibration Control')
plt.legend()
plt.grid(True)
plt.savefig('result.png')  # 保存结果至当前文件夹
plt.show()

# 绘制控制力
plt.figure(figsize=(10, 4))
plt.plot(t, F_control, label='Control Force')
plt.xlabel('Time (s)')
plt.ylabel('Force (N)')
plt.title('Control Force')
plt.legend()
plt.grid(True)
plt.savefig('control_force.png')  # 保存控制力至当前文件夹
plt.show()


print("减震比: {:.3f}".format(damping_ratio))
 