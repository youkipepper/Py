students = [
    {"name": "Tom"},
    {"name": "Jerry"}
]

# 在学员列表中搜索指定的姓名
findName = "Spike"

for stuDict in students:

    print(stuDict)

    if stuDict["name"] == findName:
        print("找到了 %s" % findName)

        # 如果已经找到, 应该直接退出循环, 而不再遍历后续元素
        break

print("抱歉没有找到 %s" % findName)
