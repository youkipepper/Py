import pymysql
import numpy as np
import matplotlib.pyplot as plt

# 连接数据库
conn = pymysql.connect(
    host='123.60.191.124',  # MySQL服务器地址
    user='root',  # 用户名
    password='Hzk2022@',  # 密码
    database='bridge'  # 数据库名称
)


def get_table_names():
    """
    获取所有以'table'开头的表名
    """
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    table_names = [table[0]
        for table in tables if table[0].startswith('table')]
    return table_names


def process_data(table_name):
    """
    处理给定表中的数据并生成频谱图
    """
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT y_offset, video_record_time, test_point_code FROM {table_name}")
    data = cursor.fetchall()

    # 获取所需数据范围内的记录
    selected_data = []
    for row in data:
        if 10 <= row[1].hour < 12:  # 时间在上午10点到12点之间
            selected_data.append(row)

    # 对于每个测点编号
    unique_test_points = set([row[2] for row in selected_data])
    for test_point in unique_test_points:
        x_values = []
        y_values = []

        # 提取位移数据和时间
        for row in selected_data:
            if row[2] == test_point:
                x_values.append(row[1])
                y_values.append(row[0])

        # 进行傅立叶变换
        fft_values = np.fft.fft(y_values)

        # 定义固定采样率为20Hz
        sampling_rate = 20

        # 进行傅立叶变换
        fft_values = np.fft.fft(y_values)

        # 计算时间间隔
        time_interval = 1 / sampling_rate

        # 确定目标频率范围为20Hz
        target_frequency_range = 20
        target_num_samples = int(target_frequency_range * time_interval)

        # 获取新的频率数组
        frequency = np.fft.fftfreq(len(y_values), d=time_interval)[:target_num_samples]

        # 在绘制之前，确保frequency和fft_values具有相同的长度
        frequency = frequency[:len(y_values)]
        fft_values = fft_values[:len(y_values)]

        # 绘制频谱图
        plt.plot(frequency, np.abs(fft_values))
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        plt.title(f'Frequency Spectrum - Test Point {test_point}')
        plt.savefig(f'{table_name}_{test_point}_spectrum.png')  # 保存频谱图为PNG文件
        plt.close()

    cursor.close()

# 获取所有以'table'开头的表名
table_names = get_table_names()

# 对每个表执行操作
for table_name in table_names:
    process_data(table_name)

# 关闭数据库连接
conn.close()
