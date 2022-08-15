#假设: 以上内容是从网络上抓取的
# 要求:
# 1、将字符串的空白字符全部去掉
# 2、再使用 " " 作为分隔符, 拼接成一个整齐的字符
poemStr = "登黄鹤楼\t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t\t 欲穷千里目 \t \n 更上一层楼"

print(poemStr)

# 1、拆分字符串
poemList = poemStr.split()
print(poemList)

# 2、合并字符串
result = " ".join(poemList)
print(result)
