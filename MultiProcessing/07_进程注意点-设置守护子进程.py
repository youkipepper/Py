import time
import multiprocessing


def work():
    # 子进程工作 2 秒
    for i in range(10):
        print("工作中...")
        time.sleep(0.2)


if __name__ == '__main__':
    work_process = multiprocessing.Process(target=work)
    work_process.daemon = True
    work_process.start()

    # 主进程睡眠 1 秒
    time.sleep(1)
    print("主进程执行完成...")

    
