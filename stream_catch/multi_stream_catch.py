import subprocess
import threading
import time
import requests
import os
import re
from datetime import datetime
import sys

# 使用线程局部存储来跟踪每个线程的状态
thread_local = threading.local()

def create_directory_for_serial_number(serial_number):
    directory_name = f"./{serial_number}"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    return directory_name

def extract_serial_number(url):
    match = re.search(r"/([A-Z0-9]+?)/0/0/", url)
    return match.group(1) if match else None

def check_stream_url(url):
    try:
        with requests.get(url, stream=True, timeout=10) as response:
            return response.ok
    except requests.RequestException as e:
        print(f"无法连接到直播流地址: {e}")
        return False

def rename_temp_file(directory_name, serial_number, start_time):
    end_time = datetime.now()
    end_time_str = end_time.strftime("%Y%m%d_%H%M%S")
    start_time_str = datetime.fromtimestamp(start_time).strftime("%Y%m%d_%H%M%S")
    temp_output_file = os.path.join(directory_name, f"temp_output_{serial_number}.mp4")
    final_output_file = os.path.join(directory_name, f"video_{serial_number}_{start_time_str}_to_{end_time_str}.mp4")
    if os.path.exists(temp_output_file):
        os.rename(temp_output_file, final_output_file)
        print(f'[{serial_number}] 视频已保存到: {final_output_file}')

def record_stream(stream_url):
    thread_local.interrupted = False

    serial_number = extract_serial_number(stream_url)
    if serial_number is None:
        print(f"无法从URL {stream_url} 中提取序列号。")
        return

    if not check_stream_url(stream_url):
        print(f"直播地址 {stream_url} 无效或无法访问。")
        return

    directory_name = create_directory_for_serial_number(serial_number)

    while not thread_local.interrupted:
        start_time = time.time()
        temp_output_file = os.path.join(directory_name, f"temp_output_{serial_number}.mp4")
        command = ["ffmpeg", "-i", stream_url, "-t", "15", "-c", "copy", "-bsf:a", "aac_adtstoasc", temp_output_file]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

        print(f"[{serial_number}] 开始录制视频。")
        process.wait()
        rename_temp_file(directory_name, serial_number, start_time)

def start_recording_from_file(file_path):
    with open(file_path, 'r') as file:
        stream_urls = file.read().splitlines()

    threads = []
    for url in stream_urls:
        thread = threading.Thread(target=record_stream, args=(url,))
        thread.start()
        threads.append(thread)

    try:
        while any(thread.is_alive() for thread in threads):
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n接收到中断信号，正在停止所有录制...")
        for thread in threads:
            setattr(thread_local, 'interrupted', True)
        raise

    # 确保所有线程都有机会执行清理
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    file_path = './stream_path.txt'
    start_recording_from_file(file_path)
