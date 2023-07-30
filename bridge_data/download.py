import pymysql
import csv

# 连接到MySQL数据库
conn = pymysql.connect(
    host='123.60.191.124',  # MySQL服务器地址
    user='root',  # 用户名
    password='Hzk2022@',  # 密码
    database='bridge'  # 数据库名称
)

# 创建游标对象
cursor = conn.cursor()

try:
    # 获取所有以"table"开头的表名
    cursor.execute("SHOW TABLES LIKE 'table%'")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        file_name = f"{table_name}.csv"

        # 查询表中的数据
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        # 写入CSV文件
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

        print(f"Table '{table_name}' exported to '{file_name}'")

finally:
    # 关闭游标和连接
    cursor.close()
    conn.close()