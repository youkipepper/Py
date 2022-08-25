a = 6
b = 100

print("交换前: a = %d , b = %d" % (a, b))

# 解法1-使用其他变量


def Solution1(a, b):

    c = a
    a = b
    b = c

    print("Solution1 交换后: a = %d , b = %d" % (a, b))


# 解法2-不使用其他的变量
def Solution2(a, b):
    a = a+b
    b = a-b
    a = a-b
    print("Solution2 交换后: a = %d , b = %d" % (a, b))

# 解法3-Python专有


def Solution3(a, b):
    # a, b = (b, a)
    # 提示: 等号右边是一个元组, 只是把小括号省略了
    a, b = b, a
    print("Solution3 交换后: a = %d , b = %d" % (a, b))


Solution1(a, b)
Solution2(a, b)
Solution3(a, b)
