def sumNumbers(num):
    # 1. 出口
    if num == 1:
        return 1
    # 2. 数字的累加 num + (1...num-1)
    # 假设 sumNumbers 能够正确地处理 1...num-1
    temp = sumNumbers(num-1)

    return num + temp


result = sumNumbers(100)
print(result)
