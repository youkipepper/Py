import os
import shutil
import pandas as pd

def move_small_csv_files(root_folder, threshold=500, useless_folder='./useless'):
    # 创建useless文件夹，如果不存在的话
    if not os.path.exists(useless_folder):
        os.makedirs(useless_folder)

    # 遍历文件夹及其子文件夹
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.csv'):
                file_path = os.path.join(foldername, filename)
                try:
                    # 读取CSV文件并计算行数
                    df = pd.read_csv(file_path)
                    row_count = df.shape[0]

                    # 如果行数少于或等于阈值，则移动文件
                    if row_count <= threshold:
                        # 目标路径
                        destination_path = os.path.join(useless_folder, filename)
                        shutil.move(file_path, destination_path)
                        print(f'Moved {file_path} to {destination_path}')
                except Exception as e:
                    print(f'Error processing file {file_path}: {e}')

# 调用函数，传入要处理的文件夹路径
root_folder = './data_hn'  # 替换为你的文件夹路径
move_small_csv_files(root_folder)
