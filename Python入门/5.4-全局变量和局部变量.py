def demo1():
    # 定义一个局部变量
    num = 10

    print("在 demo1 函数内部的变量是 %d" % num)


def demo2():
    # print("%d" % num)
    pass


# 在函数内部定义的变量, 不能在其他位置使用
# print("%d" % num)

demo1()
demo2()

num = 10


def demo3():
    print("demo3 ===> %d" % num)

def demo4():
    print("demo4 ===> %d" % num)

demo3()
demo4()
