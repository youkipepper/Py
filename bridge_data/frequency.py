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

# Check if the connection was successful
if conn.open:
    print("Database connection successful!")
else:
    print("Database connection failed.")

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
    处理给定表中的数据并上传到数据库
    """
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT y_offset, video_record_time, test_point_code FROM {table_name}")
    data = cursor.fetchall()

    # 获取所需数据范围内的记录
    selected_data = []
    for row in data:
        hour = row[1].hour
        if 0 <= row[1].minute < 10:  # 计算每个小时的前十分钟
            hour -= 1  # 小时减1

        if hour >= 4 and hour <= 8:  # 时间在4点到8点之间
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

        # 确定固定采样率为20Hz
        sampling_rate = 20

        # 计算时间间隔
        time_interval = 1 / sampling_rate

        # 进行傅立叶变换
        fft_values = np.fft.fft(y_values)

        # 确定目标频率范围
        target_frequency_range = np.linspace(0, sampling_rate / 2, int(len(y_values) / 2))

        # 寻找非零横坐标下的纵坐标最值点并上传到数据库
        non_zero_indices = np.where((target_frequency_range >= 4) & (target_frequency_range <= 8))
        max_value_index = np.argmax(np.abs(fft_values[non_zero_indices]))
        max_x = target_frequency_range[non_zero_indices][max_value_index]
        max_y = np.abs(fft_values[non_zero_indices][max_value_index])

        # 将最值点数据上传到数据库
        query = f"INSERT INTO frequency (test_point_code, time, 1st_order_frequency, 1st_order_alpha) VALUES ('{test_point}', '{row[1].replace(minute=0)}', {max_x}, {max_y})"
        cursor.execute(query)
    
    # 提交事务
    conn.commit()
    cursor.close()


# 获取所有以'table'开头的表名
table_names = get_table_names()

# 对每个表执行操作
for table_name in table_names:
    process_data(table_name)

# 关闭数据库连接
conn.close()
