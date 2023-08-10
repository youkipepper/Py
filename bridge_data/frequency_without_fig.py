import pymysql
import numpy as np
import datetime

# 连接数据库


def connect_to_db():
    return pymysql.connect(
        host='123.60.191.124',
        user='root',
        password='Hzk2022@',
        database='bridge'
    )


# Print success message
if connect_to_db:
    print("Connected to the database successfully!")


def get_table_names(connection):
    """
    获取所有以'table'开头的表名
    """
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        table_names = [table[0]
                       for table in tables if table[0].startswith('table')]
    return table_names


def process_data(connection, table_name):
    """
    处理给定表中的数据并上传到frequency表
    """
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT y_offset, video_record_time, test_point_code FROM {table_name}")
        data = cursor.fetchall()

    # 计算目标频率范围
    sampling_rate = 20
    target_frequency_range = np.linspace(
        0, sampling_rate / 2, sampling_rate // 2)

    # 按小时处理数据
    for hour in range(24):
        for minute in range(0, 51, 10):  # 每小时前十分钟
            start_time = datetime.time(hour, minute, 0)
            end_time = datetime.time(hour, (minute + 10) % 60, 0)
            selected_data = [
                row for row in data if start_time <= row[1].time() < end_time]

            unique_test_points = set([row[2] for row in selected_data])

            for test_point in unique_test_points:
                x_values = []
                y_values = []

                for row in selected_data:
                    if row[2] == test_point:
                        x_values.append(row[1])
                        y_values.append(row[0])

                if len(x_values) > 0:
                    # 进行傅立叶变换
                    fft_values = np.fft.fft(y_values)

                    # 寻找非零横坐标下的纵坐标最值点并上传到数据库
                    non_zero_indices = np.where(
                        (target_frequency_range >= 6.1) & (target_frequency_range <= 6.5))
                    max_value_index = np.argmax(
                        np.abs(fft_values[non_zero_indices]))
                    max_x = target_frequency_range[non_zero_indices][max_value_index]
                    max_y = np.abs(
                        fft_values[non_zero_indices][max_value_index])

                    time_value = selected_data[0][1].replace(
                        minute=minute, second=0, microsecond=0)
                    insert_query = f"INSERT INTO frequency (test_point_code, time, 1st_order_frequency, 1st_order_alpha) VALUES ('{test_point}', '{time_value}', {max_x}, {max_y})"
                    cursor.execute(insert_query)
                    connection.commit()

                    print(
                        f"Uploaded data for Test Point {test_point} at {time_value}")


def main():
    # 连接数据库
    connection = connect_to_db()

    # 获取所有以'table'开头的表名
    table_names = get_table_names(connection)

    with connection.cursor() as cursor:
        # 对每个表执行操作
        for table_name in table_names:
            process_data(connection, table_name)

    # 关闭数据库连接
    connection.close()


if __name__ == "__main__":
    main()
