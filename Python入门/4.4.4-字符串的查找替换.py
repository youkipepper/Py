str = "hello world"

# 1、判断是否以指定字符串开始
print(str.startswith("hello"))

# 2、判断是否以指定字符串结束
print(str.endswith("world"))

# 3、查找指定字符串
print(str.find("llo"))

# 4、替换字符串
# 注意: 不会修改原有字符串内容
print(str.replace("world", "python"))
print(str)
