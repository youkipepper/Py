import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 设置均值和标准差
mu = 0
sigma = 1

# 生成Z分数数据
z_scores = np.linspace(-4, 4, 1000)

# 计算Z分数的概率密度
pdf = stats.norm.pdf(z_scores, mu, sigma)

# 绘制Z分数分布图像
plt.figure(figsize=(10, 6))
plt.plot(z_scores, pdf, label='标准正态分布 (μ=0, σ=1)')
plt.fill_between(z_scores, pdf, alpha=0.2)

# 标注三个标准差范围
for z in [-3, -2, -1, 0, 1, 2, 3]:
    plt.axvline(x=z, linestyle='--', color='grey')
    plt.text(z, 0.02, f'Z={z}', horizontalalignment='center')

plt.title('标准正态分布的Z分数分布图像')
plt.xlabel('Z分数')
plt.ylabel('概率密度')
plt.legend()
plt.grid(True)
plt.show()
