# 1. 打开
file_read = open("9.2-README.txt")
file_write = open("9.5-README[copy].txt", "w")

# 2. 读写
while True:
    # 读取一行内容
    text = file_read.read()
    # 判断是否读取到内容
    if not text:
        break

    file_write.write(text)

# 3. 关闭
file_read.close()
file_write.close()