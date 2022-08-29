class Cat:
    def __init__(self, newName):
        self.name = newName
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)


# Tom 是一个全局变量
Tom = Cat("Tom")
print(Tom.name)

# del 关键字可以删除一个对象
del Tom

print("-"*50)
