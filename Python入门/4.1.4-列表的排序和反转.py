numList = [6, 8, 4, 1, 10]
nameList = ["Tom", "Jerry", "Spike", "Jerry"]

# 升序
nameList.sort()  # 默认是首字母升序
numList.sort()  # 默认是升序
print(nameList)
print(numList)

# 降序
nameList.sort(reverse=True)
print(nameList)
numList.sort(reverse=True)
print(numList)

# 逆序
nameList.reverse()
print(nameList)
numList.reverse()
print(numList)
