def sumNum(num1, num2):
    """对两个数字的求和"""
    result = num1+num2
    return result  # 可以使用返回值, 告诉调用函数一方计算的结果


# 可以使用变量, 来接收函数执行的返回结果
sumResult = sumNum(10, 20)
print("计算结果: %d" % sumResult)
