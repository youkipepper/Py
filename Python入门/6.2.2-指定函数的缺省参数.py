def printInfo(name, gender=True):
    genderText = "男生"

    if not gender:
        genderText = "女生"

    print("%s 是 %s" % (name, genderText))


# 假设班上的同学, 男生居多
printInfo("小明")
printInfo("老王")
printInfo("小美",False)