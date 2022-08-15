from distutils.log import info


infoTuple = ("Tom", 20, 120)

# 使用迭代遍历元组
for item in infoTuple:
    # 使用格式字符串拼接 item这个变量不方便!
    # 因为元组中通常保存的数据类型是不同的!
    print(item)
