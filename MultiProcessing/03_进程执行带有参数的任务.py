# 1. 导入进程包
import multiprocessing
import time


def sing(num):
    for i in range(num):
        print("sing...")
        time.sleep(0.5)


def dance(num):
    for i in range(num):
        print("dance...")
        time.sleep(0.5)

if __name__ == '__main__':
    # 2. 使用进程类创建进程对象
    # target: 指定进程执行的函数
    # args: 使用元组方式给指定任务传参
    sing_process = multiprocessing.Process(target=sing, args=(3,))
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 2})

    # 3. 使用进程对象启动进程执行指定任务
    sing_process.start()

    