# 1. 导入进程包
import multiprocessing
import time

def sing():
    for i in range(3):
        print("sing...")
        time.sleep(0.5)

def dance():
    for i in range(3):
        print("dance...")
        time.sleep(0.5)

if __name__ == '__main__':
    # 2. 使用进程类创建进程对象
    # target: 指定进程执行的函数
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)

    # 3. 使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()


