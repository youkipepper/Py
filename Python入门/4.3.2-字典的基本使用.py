Tom = {"name": "Tom", }

# 1、取值
print(Tom["name"])
# print(Tom["name123"])


# 2、增加/修改
Tom["age"] = 18

# 3、删除
print(Tom)
Tom.pop("name")
print(Tom)

# 4、统计键值对数量
print(len(Tom))

# 5、合并字典
tempDic = {"height": 1.25}

# 注意: 如果被合并的字典中包含已经存在的键值对, 会覆盖原有的键值对
Tom.update(tempDic)
print(Tom)

# 6、清空字典
Tom.clear()
print(Tom)
