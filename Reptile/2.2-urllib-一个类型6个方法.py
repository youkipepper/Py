import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# response 是 HTTPResponse 类型
# print(type(response))

# 按照一个字节一个字节去读
# content = response.read()
# print(content)


# 返回 5 个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# content = response.readlines()
# print(content)

# 返回状态码, 如果是200, 那就证明逻辑错误
# print(response.getcode())

# 返回的是 url 地址
# print(response.geturl())

# 获取一个状态信息
print(response.getheaders())


# 一个类型 HTTPResponse
# 六个方法 read readline readlines getcode geturl getheaders 
