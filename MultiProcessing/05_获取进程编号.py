# 1. 导入进程包
import multiprocessing
import time
import os


def sing(num, name):
    print("唱歌进程的pid: ", os.getpid())
    print("唱歌进程的父进程pid: ", os.getppid())
    for i in range(num):
        print(name)
        print("sing...")
        time.sleep(0.5)


def dance(num, name):
    print("跳舞进程的Pid: ", os.getpid())
    print("跳舞进程的父进程pid: ", os.getppid())
    for i in range(num):
        print(name)
        print("dance...")
        time.sleep(0.5)


if __name__ == '__main__':
    # 2. 使用进程类创建进程对象
    # target: 指定进程执行的函数
    # args: 使用元组方式给指定任务传参
    #   元组的元素顺序就是任务的参数顺序
    # kwargs: 使用字典的方式给指定任务传参
    #   key名就是参数的名字

    sing_process = multiprocessing.Process(target=sing, args=(3, "xiaoming"))
    dance_process = multiprocessing.Process(
        target=dance, kwargs={"name": "Tom", "num": 2, })

    # 3. 使用进程对象启动进程执行指定任务
    sing_process.start()
    dance_process.start()