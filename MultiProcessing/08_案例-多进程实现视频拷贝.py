import os
import multiprocessing


def copy_file(file_name, source_dir, dest_dir):
    pass
    # 1. 拼接源文件路径和目标文件路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name

    # 2. 打开源文件和目标文件
    with open(source_path, "rb") as source_file:
        with open(dest_path, "wb")as dest_file:
            # 3. 循环读取源文件到目标路径
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 1. 定义源文件夹和目标文件夹
    source_dir = "/Users/youkipepper/Desktop/Py/MultiProcessing/PythonTeachVideo"
    dest_dir = "/Users/youkipepper/Desktop/Py/MultiProcessing/08_test"

    # 2. 创建目标文件夹
    try:
        os.mkdir(dest_dir)
    except:
        print("dest_dir exists.")

    # 3. 读取源文件夹的文件列表
    file_list = os.listdir(source_dir)

    # 4. 遍历文件列表实现拷贝
    for file_name in file_list:
        # copy_file(file_name, source_dir, dest_dir)

        # 5. 使用多进程实现多任务拷贝
        sub_process = multiprocessing.Process(
            target=copy_file, args=(file_name, source_dir, dest_dir))

        sub_process.start()
