import subprocess
import time
import sys
import requests
import os
import re
from datetime import datetime

def extract_serial_number(url):
    """从URL中提取摄像机序列号"""
    match = re.search(r"/([A-Z0-9]+?)/0/0/", url)
    return match.group(1) if match else None

def check_stream_url(url):
    """检查直播流地址是否有效"""
    try:
        with requests.get(url, stream=True, timeout=10) as response:
            return response.ok
    except requests.RequestException as e:
        print(f"无法连接到直播流地址: {e}")
        return False

def stop_recording(process, temp_output_file, serial_number, start_time):
    """停止录制"""
    end_time = datetime.now()
    end_time_str = end_time.strftime("%Y%m%d_%H%M%S")
    start_time_str = datetime.fromtimestamp(start_time).strftime("%Y%m%d_%H%M%S")
    final_output_file = f"output_video_{serial_number}_{start_time_str}_to_{end_time_str}.mp4"

    print('\n正在停止录制...')
    process.stdin.write(b'q')
    process.stdin.flush()
    process.wait()

    # 重命名文件
    os.rename(temp_output_file, final_output_file)

    print(f'录制已停止。视频已保存到: {final_output_file}')
    print(f'录制结束时间: {end_time_str}')
    print(f'总录制时长: {int(time.time() - start_time)} 秒')

def start_recording(stream_url, serial_number):
    """开始录制"""
    start_time = time.time()
    temp_output_file = f"temp_output_{serial_number}.mp4"
    
    command = ["ffmpeg", "-i", stream_url, "-c", "copy", "-bsf:a", "aac_adtstoasc", temp_output_file]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

    print("开始录制视频。按 Ctrl+C 结束录制。")
    print(f'录制开始时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

    try:
        while process.poll() is None:
            elapsed_time = int(time.time() - start_time)
            sys.stdout.write(f"\r已录制时长: {elapsed_time} 秒")
            sys.stdout.flush()
            time.sleep(1)
    except KeyboardInterrupt:
        stop_recording(process, temp_output_file, serial_number, start_time)

# 视频流地址
stream_url = "http://cmgw-vpc.lechange.com:8888/LCO/9C028B5PHA8CA76/0/0/20230523T050221/b8a9bb4219d4efd4b4a0ec296c4f536c.m3u8"
serial_number = extract_serial_number(stream_url)

if serial_number is None:
    print("无法从URL中提取序列号。")
    sys.exit(1)

if check_stream_url(stream_url):
    start_recording(stream_url, serial_number)
else:
    print("直播地址无效或无法访问。")


    