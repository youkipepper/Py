def sumNumber(num):
    print(num)
    # 递归的出口, 当参数满足某个条件时, 不再执行函数
    if num == 1:
        return

    # 自己调用自己
    sumNumber(num - 1)


sumNumber(3)
