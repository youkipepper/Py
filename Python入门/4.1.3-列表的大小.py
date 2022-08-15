nameList = ["Tom", "Jerry", "Spike", "Jerry"]

listLen = len(nameList)
print("列表中包含 %d 个元素" % listLen)

count = nameList.count("Jerry")
print("Jerry出现了 %d 次" % count)

nameList.remove("Jerry")  # remove 只会删除第一次出现的数据
print(nameList)
