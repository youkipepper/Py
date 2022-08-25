def demo(numList):
    print("函数内部的代码")

    # 使用方法修改列表的内容
    numList.append(9)

    print(numList)

    print("函数执行完成")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
