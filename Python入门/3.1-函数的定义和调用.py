# 注意: 定义好函数之后, 只表示这个函数封装了一段代码而已
# 如果不主动调用函数, 函数式不会主动执行的

name = "小明"


def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")


print(name)

# 只有在程序中, 主动调用函数, 才会让函数执行
say_hello()

print(name)
