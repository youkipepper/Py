from unicodedata import name


nameList = ["Tom", "Jerry", "Spike"]

# 1、取值和取索引
print(nameList[0])
print(nameList.index("Tom"))

# 2、修改
nameList[1] = "Tyke"
print(nameList[1])


# 3、增加
nameList.append("Tuffy")
print(nameList)
nameList.insert(2, "Jerry")
print(nameList)

tempList = ["Someone"]
nameList.extend(tempList)
print(nameList)

# 4、删除
nameList.remove("Someone")
print(nameList)

nameList.pop()
print(nameList)

nameList.pop(2)
print(nameList)

nameList.clear()
print(nameList)

